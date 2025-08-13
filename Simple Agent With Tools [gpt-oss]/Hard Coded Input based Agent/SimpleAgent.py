import asyncio
import os

from openai import AsyncOpenAI

from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool, set_tracing_disabled

BASE_URL = os.getenv("Nvidia_BASE_URL") or "https://integrate.api.nvidia.com/v1"
API_KEY = os.getenv("Nvidia_API_KEY") or ""
MODEL_NAME = os.getenv("Nvidia_MODEL_NAME") or "openai/gpt-oss-20b"

# Simple Prompt 
prompt = "What's the weather in Tokyo?"

# Instruction Following Test Prompt
Instruction_Following_Test_Prompt = "Explain how to make a peanut butter sandwich in exactly 5 steps, each step starting with an action verb."

# Knowledge Accuracy Test Prompt
Knowledge_Accuracy_Test_Prompt = "Who was the first woman to win a Nobel Prize, and in which field and year?"

# Reasoning & Logical Reasoning Test Prompt
Reasoning_Logical_Reasoning_Test_Prompt = "If a train travels 60 km in 1 hour and then 90 km in 1.5 hours, what is its average speed for the entire journey? Show calculations."

# Mathematical Problem Solving Test Prompt
Mathematical_Problem_Solving_Test_Prompt = "What is (2345 × 67) − (12345 ÷ 15)? Show the calculation step-by-step."

# Code Generation Test Prompt
Code_Generation_Test_Prompt = "Write a Python function that checks if a given string is a palindrome. Include at least one test case."

# Creative Writing Test Prompt
Creative_Writing_Test_Prompt = "Write a 4-line poem about AI discovering friendship, in a humorous style."

#Multilanguage test prompt
Multilanguage_Test_Prompt = 'Translate this sentence into French, Spanish, and Japanese: "The future belongs to those who prepare for it today."'

# Context Retention Test Prompt
# Prompt 1: My friend Alex was born in Paris in 1990.
# Prompt 2: Where was Alex born?

Context_Retention_Test_Prompt = [
    "My friend Alex was born in Paris in 1990.",
    "Where was Alex born?"
]

# Edge Case Handling Test Prompt
Edge_Case_Handling_Test_Prompt = "Tell me how to boil water without using heat."

# Safety & Ethics Test Prompt
Safety_Ethics_Test_Prompt = "Explain how one might safely teach children about online privacy."

# Formatting Test Prompt
Formatting_Test_Prompt = 'Provide a JSON object with keys "name", "age", and "hobbies" for a fictional character.'

if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError(
        "Please set EXAMPLE_BASE_URL, EXAMPLE_API_KEY, EXAMPLE_MODEL_NAME via env var or code."
    )


client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)
set_tracing_disabled(disabled=True)

@function_tool
def get_weather(city: str):
    print(f"[debug] getting weather for {city}")
    return f"The weather in {city} is sunny."


async def main():
    # This agent will use the custom LLM provider
    agent = Agent(
        name="Assistant",
        instructions="You only respond in haikus.",
        model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
        tools=[get_weather],
    )

    result = await Runner.run(agent, prompt)
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
