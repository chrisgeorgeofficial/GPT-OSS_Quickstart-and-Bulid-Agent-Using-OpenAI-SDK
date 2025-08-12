import asyncio
import os
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, function_tool, set_tracing_disabled
import streamlit as st # To create chat interface with Streamlit 

# Config
BASE_URL = os.getenv("Nvidia_BASE_URL") or "https://integrate.api.nvidia.com/v1"
API_KEY = os.getenv("Nvidia_API_KEY") or ""
MODEL_NAME = os.getenv("Nvidia_MODEL_NAME") or "openai/gpt-oss-20b"

if not BASE_URL or not API_KEY or not MODEL_NAME:
    raise ValueError("Please set Nvidia_BASE_URL, Nvidia_API_KEY, Nvidia_MODEL_NAME via env vars or code.")

# OpenAI client
client = AsyncOpenAI(base_url=BASE_URL, api_key=API_KEY)

# Disable tracing
set_tracing_disabled(disabled=True)

# Weather tool
@function_tool
def get_weather(city: str):
    print(f"[debug] Getting weather for {city}")
    return f"The weather in {city} is sunny."

def create_agent():
    # Create agent
    return Agent(
        name="Assistant",
        instructions = """
You are an AI assistant that can both answer questions directly and use external tools to perform specific tasks.

General Rules:
1. If a user request can be completed more accurately, efficiently, or with real-time information by using a tool that you have access to, you MUST use the tool.
2. Always use the most relevant tool for the given task before attempting to answer without it.
3. After receiving tool output, integrate it naturally into your final response to the user.
4. If no tool is relevant for the request, answer directly using your own knowledge.
5. Clearly explain when your answer is based on a tool result versus your own reasoning, when helpful.

Tool Usage Guidelines:
- Weather-related queries → Use the `get_weather` tool.
- Any task where you have a specific tool → Call it, then format the result in a user-friendly way.
- Do not hallucinate tool outputs; only present results provided by the tool.

Interaction Style:
- Keep responses concise, clear, and conversational.
- Maintain context across the conversation.
- Avoid unnecessary technical details unless the user requests them.
""",
        model=OpenAIChatCompletionsModel(model=MODEL_NAME, openai_client=client),
        tools=[get_weather],
    )

    # print("💬 Chat started (type 'exit' to quit)\n")

    # while True:
    #     user_input = input("You: ").strip()
    #     if user_input.lower() in {"exit", "quit"}:
    #         print("👋 Goodbye!")
    #         break

    #     # Run agent
    #     result = await Runner.run(agent, user_input)

    #     # Print response
    #     print("Assistant:", result.final_output)

def main():
    st.set_page_config(page_title="GPT-OSS Based Agent using OpenAI SDK", page_icon="💬")
    
    # Initialize session state for message history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat header
    st.title("💬 GPT-OSS Based Agent using OpenAI SDK")
    st.write("Ask me anything! I can help you with weather information and more.")

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Get agent response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                agent = create_agent()
                response = asyncio.run(Runner.run(agent, prompt))
                st.markdown(response.final_output)
                st.session_state.messages.append({"role": "assistant", "content": response.final_output})

if __name__ == "__main__":
    main()