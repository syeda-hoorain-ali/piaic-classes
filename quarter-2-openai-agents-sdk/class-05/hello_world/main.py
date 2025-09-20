import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, OpenAIChatCompletionsModel, function_tool, set_default_openai_api, set_default_openai_client, set_tracing_disabled


# Setup for Api Keys
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")


# Which LLM Service?
external_client = AsyncOpenAI(
    api_key=gemini_api_key, # House key
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/", # House address
)


# Global Setup for Connecting to Gemini
set_tracing_disabled(disabled=True)
set_default_openai_client(client=external_client)
set_default_openai_api("chat_completions")


# # Which LLM Model?
# llm_model = OpenAIChatCompletionsModel(
#     model="gemini-2.5-flash", # or  gemini-2.0-flash
#     openai_client=client
# )


# Create Agent
agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant",
    model="gemini-2.5-flash",
)

# Running Synchronously
result = Runner.run_sync(agent, "Hello")
print(result.final_output)
