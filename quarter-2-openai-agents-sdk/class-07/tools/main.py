import json
import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, Runner, function_tool
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
# ======================== Tools ========================
# =======================================================


# Create tool
@function_tool
def addition(a: int, b: int):
    return a + b

@function_tool
def substraction(a: int, b: int):
    return a - b


# Create Agent with tools
agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant",
    model="gemini-2.5-flash",
    tools=[addition, substraction],
)

# Running Synchronously
result = Runner.run_sync(agent, "add 5 and 3?")
print(result.final_output)


# =======================================================
# ==================== Agent as Tool ====================
# =======================================================


agentic_ai_expert = Agent(
    name="Agentic AI expert",
    instructions="You are a Agentic AI Expert ai agent.",
    model="gemini-2.5-flash",
)

agai_tool = agentic_ai_expert.as_tool(
    tool_name="agentic_ai_expert",
    tool_description="You are a helpful assistant"
)

agent2 = Agent(
    name="Assistant", # Orchistrator 
    instructions="You are a helpful assistant",
    model="gemini-2.5-flash",
    tools=[addition, substraction, agai_tool],
)

# Running Synchronously
result = Runner.run_sync(agent, "which agentic ai python framework is best for beginers")



# =======================================================

from agents import FunctionTool
import json

for tool in agent2.tools:
    if isinstance(tool, FunctionTool):
        print(tool.name)
        print(tool.description)
        print(json.dumps(tool.params_json_schema, indent=2))


# =======================================================
# ======= Hosted Tools (need paid openai api key) =======
# =======================================================

import os
from agents import Agent, FileSearchTool, Runner, WebSearchTool

# Save openai key in .env file

agent3 = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    tools=[WebSearchTool(), FileSearchTool(vector_store_ids=["your-vector-store-id"])]
)

# Running Synchronously
result = Runner.run_sync(agent, "what is today date & time")
print(result.final_output)


