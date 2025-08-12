import os
import getpass

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY") or ""

from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = NVIDIA_API_KEY
)

# Simple Prompt 
prompt = "What's the weather in Tokyo?"

strawberry_prompt = """
How many 'r's in strawberry?
"""

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


math_prompt = """
The 9 members of a baseball team went to an ice cream parlor after their game. Each player had a singlescoop cone of chocolate, vanilla, or strawberry ice cream. At least one player chose each flavor, and the number of players who chose chocolate was greater than the number of players who chose vanilla, which was greater than the number of players who chose strawberry. Let $N$ be the number of different assignments of flavors to players that meet these conditions. Find the remainder when $N$ is divided by 1000.

Please provide your answer in boxed format.
"""

response = client.responses.create(
  model="openai/gpt-oss-20b",
  input=[math_prompt],
  reasoning={"effort" : "high"},
  max_output_tokens=16384,
  top_p=0.7,
  temperature=0.6,
  stream=True
)

reasoning_done = False
for chunk in response:
  if chunk.type == "response.reasoning_text.delta":
    print(chunk.delta, end="")
  elif chunk.type == "response.output_text.delta":
    if not reasoning_done:
      print("\n")
      reasoning_done = True
    print(chunk.delta, end="")