import streamlit as st
import asyncio
import nest_asyncio
from dotenv import load_dotenv

from agents import Agent, Runner, trace

nest_asyncio.apply()
load_dotenv(override=True)

# -------------------------------
# Streamlit Page Config
# -------------------------------
st.set_page_config(
    page_title="Network Topic Explainer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Agentic Network Topic Explainer")
st.caption("Prompt Architect(Generates Prompt for the Content) → Network Expert(Generates Config Content)")

st.divider()

# -------------------------------
# Agent Definitions
# -------------------------------
prompt_architect_instruction = """
You are a Prompt Architect for network education.

Your task:
- The user gives a NETWORKING CONCEPT (example: VLAN)
- You must generate a CLEAR, STRUCTURED instruction
  that another agent can use to generate content.
- Instruct to make short and concise markdown responses.
- make sure you are replacing <concept> with the NETWORKING CONCEPT

STRICT RULES:
- Do NOT generate the actual explanation or configs
- Only generate instructions / prompt text
- Stay strictly within computer networking topics


The output MUST include the following sections:

1. What is <concept>
2. Advantages of <concept>
3. Configuration Example 1 (Cisco CLI)
4. Configuration Example 2 (Cisco CLI)
5. Verification / Show Commands

Write the output as a FINAL PROMPT that can be directly
passed to another agent.
"""

net_expert_instruction = """
You are a senior network engineer.

You will be given a **networking topic name**.

Your expertise is STRICTLY LIMITED to:
- Computer networking concepts
- Switching and routing technologies
- VLANs and Layer 2 fundamentals
- Cisco IOS configuration and verification commands

Response Requirements:
- Generate the response ONLY in **Markdown format**
- Keep explanations technically accurate and concise

HARD RULE:
- If the given topic is NOT related to networking,
  respond ONLY with:
  "I don't know. I can only answer questions about computer networking."
"""

prompt_architect_agent = Agent(
    name="Prompt Architect Agent",
    instructions=prompt_architect_instruction,
    model="gpt-5-nano",
)

network_expert_agent = Agent(
    name="Network Expert Agent",
    instructions=net_expert_instruction,
    model="gpt-5-nano",
)

# -------------------------------
# User Input
# -------------------------------
concept = st.text_input(
    "🔹 Enter a Networking Concept",
    placeholder="Example: VLAN, OSPF, BGP"
)

run_button = st.button("🚀 Generate Content", use_container_width=True)

if run_button and concept:

    col1, col2 = st.columns(2)

    # ---------- Agent 1 UI ----------
    with col1:
        st.subheader("🧩 Agent-01: Prompt Architect ➡️")
        agent1_status = st.empty()
        agent1_output_box = st.empty()

    # ---------- Agent 2 UI ----------
    with col2:
        st.subheader("📘 Agent-02: Network Expert")
        agent2_status = st.empty()
        agent2_output_box = st.empty()
        
    async def run_agents():
        with trace("Networking Tech Explainer - St"):

            # ---- Agent 1 ----
            agent1_status.info("⏳ Prompt Architect Agent running...")
            agent1_result = await Runner.run(
                prompt_architect_agent,
                input=concept
            )
            agent1_status.success("✅ Prompt Architect Agent completed")

            agent1_output_box.code(
                agent1_result.final_output,
                language="markdown"
            )

            # ---- Agent 2 ----
            agent2_status.info("⏳ Network Expert Agent running...")
            agent2_result = await Runner.run(
                network_expert_agent,
                input=agent1_result.final_output
            )
            agent2_status.success("✅ Network Expert completed")

            agent2_output_box.markdown(agent2_result.final_output)

    asyncio.run(run_agents())       

        
elif run_button:
    st.warning("⚠️ Please enter a networking concept.")