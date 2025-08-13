GPT-OSS NVIDIA API – Streamlit Agent Starter
This repository contains a Streamlit-based chat interface powered by GPT-OSS models via the NVIDIA API.
The included Python script demonstrates how to:

Connect to NVIDIA’s GPT-OSS model.

Use external tools (e.g., weather lookup) inside an AI conversation.

Maintain chat history in a web app.

✨ Features
💬 Chat Interface – Built with Streamlit for a clean, interactive UI.

🔌 NVIDIA API Integration – Works with GPT-OSS via the NVIDIA API.

🛠 Tool Support – Example weather tool included (easy to extend).

📜 Conversation Memory – Keeps context throughout the session.

⚡ Quick Start – Just plug in your API key and run.

1. Clone the repository

git clone <repo_url>
cd <repo_name>

2.Install dependencies

pip install -r requirements.txt

3.Set up environment variables

Create a .env file based on .env.example

4. Add your NVIDIA API key from:

https://build.nvidia.com/openai/gpt-oss-20b

(Using .env ensures your key stays secure)

5. Run the script

python simpleagent.py

🛠 Customization
Add your own tools by defining functions with the @function_tool decorator.

Modify the agent instructions in create_agent() to change behavior.

Adjust the model parameters in the agent setup for different output styles.
