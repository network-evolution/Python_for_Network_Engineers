import streamlit as st
from google import genai
from pydantic import BaseModel, Field
from typing import Union, List, Optional
from dotenv import load_dotenv
import os

# Load local environment variables
load_dotenv(override=True)

# --- 1. Define Schemas ---
class NetworkingTopic(BaseModel):
    is_networking_related: bool = Field(description="Whether the input topic is related to computer networking.")
    category: Optional[str] = Field(description="The category of networking (e.g., Routing, Security, Wireless).")
    confidence_score: float = Field(description="Confidence score from 0.0 to 1.0.")

class NetworkingExplanation(BaseModel):
    topic_name: str
    definition: str
    core_concepts: List[str]
    config_example: str
    best_practices: List[str]

# --- 2. App Configuration ---
st.set_page_config(page_title="Network Expert AI", page_icon="🌐", layout="wide")
st.title("🌐 Networking Knowledge Agent")

# Sidebar for Configuration
with st.sidebar:
    st.header("Settings")
    # Priority: Sidebar Input > .env file
    env_key = os.getenv("GEMINI_API_KEY", "")
    user_key = st.text_input("Override Gemini API Key", type="password", help="Leave blank to use the .env file key.")
    
    final_api_key = user_key if user_key else env_key
    threshold = st.slider("Gatekeeper Confidence Threshold", 0.0, 1.0, 0.7)
    
    if not final_api_key:
        st.warning("⚠️ No API Key detected in .env or Sidebar.")
    else:
        st.success("✅ API Key Ready")

# --- 3. Main Logic ---
user_input = st.text_input("Enter a Networking Topic:", placeholder="e.g., BGP, DHCP, OSPF, Subnetting")

if st.button("Analyze & Generate") and user_input:
    if not final_api_key:
        st.error("Please provide an API key in the sidebar or a .env file to continue.")
    else:
        client = genai.Client(api_key=final_api_key)
        
        # --- STAGE 1: Gatekeeper Agent ---
        with st.status("Agent 1: Gatekeeper classifying topic...", expanded=True) as status:
            gatekeeper_prompt = f"Identify if the following topic is related to computer networking: '{user_input}'"
            
            try:
                response = client.models.generate_content(
                    model="gemini-2.0-flash",
                    contents=gatekeeper_prompt,
                    config={
                        "response_mime_type": "application/json",
                        "response_json_schema": NetworkingTopic.model_json_schema(),
                    },
                )
                classification = NetworkingTopic.model_validate_json(response.text)
                
                if classification.is_networking_related and classification.confidence_score >= threshold:
                    st.write(f"✅ **Validated:** {classification.category}")
                    st.write(f"Confidence: {classification.confidence_score:.2f}")
                    status.update(label="Topic Approved by Gatekeeper", state="complete", expanded=False)
                    is_valid = True
                else:
                    st.write(f"❌ **Rejected:** Confidence {classification.confidence_score:.2f}")
                    status.update(label="Topic Rejected", state="error", expanded=False)
                    st.error(f"'{user_input}' does not appear to be a networking-specific topic.")
                    is_valid = False
            except Exception as e:
                st.error(f"Gatekeeper Error: {e}")
                is_valid = False

        # --- STAGE 2: Expert Agent (Triggered only if valid) ---
        if is_valid:
            with st.status("Agent 2: Expert generating documentation...", expanded=True) as status:
                expert_prompt = f"""
                You are a Senior Network Engineer. Generate a detailed technical explanation for: {user_input}.
                Include a definition, core concepts, a practical configuration example, and best practices.
                """
                
                try:
                    response = client.models.generate_content(
                        model="gemini-2.0-flash",
                        contents=expert_prompt,
                        config={
                            "response_mime_type": "application/json",
                            "response_json_schema": NetworkingExplanation.model_json_schema(),
                        },
                    )
                    explanation = NetworkingExplanation.model_validate_json(response.text)
                    status.update(label="Documentation Generated!", state="complete", expanded=False)
                    
                    # --- FINAL OUTPUT DISPLAY ---
                    st.divider()
                    st.header(f"📘 {explanation.topic_name}")
                    
                    # Add a visual aid for the topic
                    st.write(f"")
                    
                    st.subheader("Definition")
                    st.info(explanation.definition)
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.subheader("Core Concepts")
                        for concept in explanation.core_concepts:
                            st.markdown(f"- **{concept}**")
                    
                    with col2:
                        st.subheader("Best Practices")
                        for bp in explanation.best_practices:
                            st.markdown(f"- {bp}")

                    st.subheader("Configuration Example")
                    st.code(explanation.config_example, language="bash")
                    
                except Exception as e:
                    st.error(f"Expert Agent Error: {e}")