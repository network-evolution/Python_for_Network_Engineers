import streamlit as st
from google import genai
from pydantic import BaseModel, Field
from typing import Union, Literal, Optional
from dotenv import load_dotenv
from netmiko import ConnectHandler
import os
import json

# Load environment variables
load_dotenv(override=True)

# --- 1. Define Schemas ---
class DangerousConfig(BaseModel):
    hostname: str = Field(description="The hostname of the device provided in the prompt.")
    risk_level: Literal["High", "Critical"] = Field(description="Severity of the change.")
    impact_analysis: str = Field(description="Explanation of what will break.")
    confidence_score: float = Field(description="Score from 0.0 to 1.0.")

class StandardChange(BaseModel):
    hostname: str = Field(description="The hostname of the device provided in the prompt.")
    change_summary: str = Field(description="Brief summary of the change.")
    affected_interface: Optional[str] = Field(description="Interface being modified, if any.")
    confidence_score: float = Field(description="Score from 0.0 to 1.0.")

class ConfigAnalysisResult(BaseModel):
    decision: Union[DangerousConfig, StandardChange]

# --- 2. Helper Functions ---

def load_inventory_data():
    """Reads the inventory file and returns the dictionary."""
    if os.path.exists("inventory.json"):
        with open("inventory.json", "r") as f:
            return json.load(f)
    return {}

def get_device_credentials(hostname: str, inventory: dict):
    """Retrieves credentials from the loaded inventory dict."""
    return inventory.get(hostname)

def run_netmiko_push(hostname: str, commands: str, inventory: dict):
    """
    Connects to device, pushes config, and returns the output log.
    """
    device_params = get_device_credentials(hostname, inventory)
    
    if not device_params:
        return f"❌ Error: Device '{hostname}' not found in inventory."

    log_output = []
    log_output.append(f"🔌 Connecting to {device_params['host']}...")
    
    try:
        with ConnectHandler(**device_params) as net_connect:
            log_output.append("🔓 Connection Successful. Entering Config Mode...")
            
            config_set = commands.splitlines() 
            output = net_connect.send_config_set(config_set)
            
            log_output.append("\n📄 --- DEVICE TERMINAL OUTPUT ---")
            log_output.append(output)
            log_output.append("----------------------------------")
            log_output.append("✅ Configuration Pushed Successfully.")
            
        return "\n".join(log_output)

    except Exception as e:
        return f"❌ Netmiko Failed: {str(e)}"

def analyze_config_with_gemini(hostname, config_snippet):
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    
    prompt = f"""
    You are a Network Engineering expert. Analyze the following configuration snippet for safety.

    Target Device Hostname: {hostname}
    Config Snippet: '{config_snippet}'

    Instructions:
    1. Always include the 'hostname' provided above in your JSON response.
    2. If the config causes an outage or drops connectivity, it is Dangerous.
    3. If it is benign (description change, new interface), it is Standard.
    """
    
    response = client.models.generate_content(
        model="gemini-2.0-flash-exp", 
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_json_schema": ConfigAnalysisResult.model_json_schema(),
        },
    )
    return ConfigAnalysisResult.model_validate_json(response.text)

# --- 3. Streamlit UI Layout ---

st.set_page_config(page_title="AI Network Gatekeeper", layout="wide")

st.title("🛡️ AI Network Config Gatekeeper Agent")
st.markdown("Select a device and enter configuration. The AI will analyze safety before deployment.")

# --- Load Inventory Data ---
inventory_data = load_inventory_data()
available_hosts = list(inventory_data.keys())

# Sidebar
with st.sidebar:
    st.header("Device Inventory Status")
    if available_hosts:
        st.success(f"Loaded {len(available_hosts)} devices")
        # st.json(inventory_data)
    else:
        st.error("No devices found in inventory.json")

# Main Input Form
col1, col2 = st.columns([1, 2])

with col1:
    # UPDATED: Using Selectbox for Dropdown
    if available_hosts:
        hostname_input = st.selectbox("Select Target Device", options=available_hosts)
    else:
        hostname_input = st.text_input("Target Hostname (Manual Entry)")

with col2:
    config_input = st.text_area("Configuration Snippet", height=150, placeholder="interface Loopback0\n description Added by AI Agent")

analyze_btn = st.button("Analyze & Auto-Deploy", type="primary")

# --- 4. Main Application Logic ---

if analyze_btn:
    if not hostname_input or not config_input:
        st.warning("Please select a device and provide configuration.")
    else:
        # Step 1: AI Analysis
        with st.spinner("🤖 AI is analyzing impact..."):
            try:
                result = analyze_config_with_gemini(hostname_input, config_input)
                decision = result.decision
                
                # Create a container for the results
                result_container = st.container()
                
                # CASE 1: Dangerous Config
                if isinstance(decision, DangerousConfig):
                    result_container.error(f"⛔ BLOCKED: {decision.risk_level} Risk Detected")
                    result_container.markdown(f"**Impact Analysis:** {decision.impact_analysis}")
                    result_container.metric("Confidence Score", f"{decision.confidence_score:.2f}")
                
                # CASE 2: Standard Change (Safe)
                elif isinstance(decision, StandardChange):
                    result_container.success("✅ APPROVED: Standard Change Detected")
                    result_container.markdown(f"**Summary:** {decision.change_summary}")
                    
                    col_a, col_b = result_container.columns(2)
                    col_a.metric("Confidence Score", f"{decision.confidence_score:.2f}")
                    if decision.affected_interface:
                        col_b.metric("Affected Interface", decision.affected_interface)
                    
                    # Step 2: Automation Execution (Only if Safe)
                    st.divider()
                    st.subheader("🚀 Automation Output")
                    
                    with st.status("Connecting to device...", expanded=True) as status:
                        st.write(f"Initiating connection to {hostname_input}...")
                        
                        # Pass inventory_data to the function so we don't read the file again
                        log_output = run_netmiko_push(decision.hostname, config_input, inventory_data)
                        
                        st.code(log_output, language="bash")
                        
                        if "Netmiko Failed" in log_output:
                            status.update(label="Deployment Failed", state="error")
                        else:
                            status.update(label="Deployment Complete", state="complete")

            except Exception as e:
                st.error(f"System Error: {e}")