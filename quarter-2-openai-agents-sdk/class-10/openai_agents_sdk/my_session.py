import asyncio
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import set_default_openai_api, set_default_openai_client, set_tracing_disabled

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
# ==================== SQLiteSession ====================
# =======================================================

from agents import Agent, Runner, SQLiteSession

async def main():

    # Create agent
    agent = Agent(
        name="Assistant",
        instructions="Reply very concisely.",
        model="gemini-2.5-flash",
    )

    # Create a session instance with a session ID
    session = SQLiteSession("conversation_123")
    # session = SQLiteSession("conversation_123", db_path="conversations.db")

    # First turn
    result = await Runner.run(
        agent,
        "Hello! My name is Hoorain",
        session=session,
    )
    print(result.final_output)

    # Second turn - agent automatically remembers previous context
    result = await Runner.run(
        agent,
        "What is my name?",
        session=session
    )
    print(result.final_output)


asyncio.run(main())
