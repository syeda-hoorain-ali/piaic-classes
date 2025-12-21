import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import set_default_openai_api, set_default_openai_client, set_tracing_disabled
from agents import enable_verbose_stdout_logging

# Debug every step
enable_verbose_stdout_logging()

# Setup for Api Keys
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Which LLM Service?
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Global Setup for Connecting to Gemini
set_tracing_disabled(disabled=True)
set_default_openai_client(client=external_client)
set_default_openai_api("chat_completions")


# =======================================================
# ====================== Handsoff =======================
# =======================================================

from agents import Agent, Runner, handoff
import asyncio

billing_agent = Agent(name="Billing agent", instructions="Handle billing questions.")
refund_agent  = Agent(name="Refund agent",  instructions="Handle refunds.")

triage_agent = Agent(
    name="Triage agent",
    instructions=(
        "Help the user with their questions. "
        "If they ask about billing, handoff to the Billing agent. "
        "If they ask about refunds, handoff to the Refund agent."
    ),
    handoffs=[billing_agent, handoff(refund_agent)],  # either direct agent or `handoff(...)`
)

async def main():
    result = await Runner.run(triage_agent, "I need to check refund status.")
    print(result.final_output)
    print(result.last_agent)

asyncio.run(main())
