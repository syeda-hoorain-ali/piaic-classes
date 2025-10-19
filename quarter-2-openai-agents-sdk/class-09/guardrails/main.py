import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import set_default_openai_api, set_default_openai_client, set_tracing_disabled
# from agents import enable_verbose_stdout_logging

# Debug every step
# enable_verbose_stdout_logging()

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
# ===================== Guardrails ======================
# =======================================================

from pydantic import BaseModel
from agents import Agent, Runner, input_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered

class MathHomeworkOutput(BaseModel):
    reasoning: str
    is_math_homework: bool

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking you to do their math homework.",
    output_type=MathHomeworkOutput,
    model="gemini-2.5-flash",
)


# @input_guardrail
# async def math_guardrail(ctx, agent, input) -> GuardrailFunctionOutput:
#     if "math" in input:
#         return GuardrailFunctionOutput(
#             output_info="The user is asking about math",
#             tripwire_triggered=True
#         )
#     else:
#         return GuardrailFunctionOutput(
#             output_info="The user is not asking about math",
#             tripwire_triggered=False
#         )


@input_guardrail
async def math_guardrail(ctx, agent, input) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input)
    print("Math guardrail final output:", result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_math_homework,
    )


agent = Agent(
    name="Customer support agent",
    instructions="You are a customer support agent. You help customers with their questions.",
    input_guardrails=[math_guardrail],
    model="gemini-2.5-flash",
)

try:
    result = Runner.run_sync(agent, "solve this problem: x: 2x + 3 = 11?")
    print("Guardrail didn't trip - this is unexpected")
    print(result.final_output)

except InputGuardrailTripwireTriggered:
    print("Math homework guardrail tripped")
