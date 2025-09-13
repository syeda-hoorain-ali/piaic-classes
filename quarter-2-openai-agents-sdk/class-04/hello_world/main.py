import os
from dotenv import find_dotenv, load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, set_tracing_disabled


# 🔐 Step 1: Setup for Api Keys
load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")


# 🌐 Step 2: Client Setup for Connecting to Gemini
set_tracing_disabled(disabled=True)

# 1. Which LLM Service?
external_client: AsyncOpenAI = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# 2. Which LLM Model?
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash", # gemini-2.0-flash
    openai_client=external_client
)

# 💬 Step 3 Running Agent Synchronously
agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant"
)

result = Runner.run_sync(
    starting_agent=agent, 
    input="Write a haiku about recursion in programming."
)

print(result.final_output)
