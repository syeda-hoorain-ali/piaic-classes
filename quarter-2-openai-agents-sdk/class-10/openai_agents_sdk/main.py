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
# ======================= Memory ========================
# =======================================================

from agents import Agent, Runner, TResponseInputItem

history: list[TResponseInputItem] = []

async def main():

    agent = Agent(
        name="Assistant",
        model="gemini-2.5-flash",
    )

    result1 = await Runner.run(agent, "Hello my name is Hoorain")
    print("User: Hello my name is Hoorain")
    print("Agent:", result1.final_output)
    history.extend(result1.to_input_list())


    print('='*40)


    result2 = await Runner.run(
        starting_agent=agent,
        input=history + [{"role": "user", "content": "What is my name?"}]
        # context=user_info,
    )
    print("User: What is my name?")
    print("Agent:", result2.final_output)
    history.extend(result2.to_input_list())


asyncio.run(main())