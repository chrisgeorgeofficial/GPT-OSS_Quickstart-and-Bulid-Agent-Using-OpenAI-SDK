### **GPT-OSS NVIDIA API – Testing \& Starter Code**



**This repository provides a ready-to-use Python testing suite for evaluating GPT-OSS models via the NVIDIA API.**

**It comes with a diverse set of prompt categories—ranging from simple Q\&A to complex reasoning, coding, multilingual support, and ethical AI tests—making it the perfect quick-start toolkit for developers looking to validate and benchmark GPT-OSS capabilities.**



**✨ Key Features**

**🔌 Plug \& Play – Just add your NVIDIA API key and run the script.**



**📚 Comprehensive Prompt Categories**



**✅ Simple Prompts \& Q\&A**



**🧠 Logical Reasoning \& Math Problems**



**💻 Code Generation \& Snippets**



**🌍 Multi-Language Translation \& Support**



**✍️ Creative Writing \& Text Formatting**



**🛡️ Safety, Ethics \& Responsible AI Prompts**



**📄 Structured Data (JSON) Generation**



**⚡ Real-Time Streaming – Watch the model’s response generate live in your terminal.**



**🔧 Easily Extendable – Add custom prompts to the suite in seconds.**



**📦 Setup**



1. **Clone the repository**



**git clone <repo\_url>**

**cd <repo\_name>**



**2.Install dependencies**



**pip install -r requirements.txt**



**3.Set up environment variables**



**Create a .env file based on .env.example**



**4. Add your NVIDIA API key from:**



**https://build.nvidia.com/openai/gpt-oss-20b**

**(Using .env ensures your key stays secure)**



**5. Run the script**



**python gpt-oss-starter.py**



**🛠 Usage \& Customization**

**You can modify model parameters in the script to tailor your testing.**

**Example:**



**response = client.responses.create(**

    **model="openai/gpt-oss-20b",**

    **input=\[math\_prompt],**

    **reasoning={"effort": "high"},**

    **max\_output\_tokens=16384,**

    **top\_p=0.7,**

    **temperature=0.6,**

    **stream=True**

**)**

**temperature – Controls creativity (0.0 = deterministic, 1.0 = more random)**



**top\_p – Nucleus sampling for diversity control**



**max\_output\_tokens – Maximum tokens in the output**



**reasoning – Effort level for complex reasoning tasks**



**stream – Enables live response streaming**



**📄 Prompt Categories Included :**



**Basic Q\&A – Simple factual and conversational queries**



**Logical Reasoning \& Math – Problem-solving and numerical tasks**



**Code Generation – Python, JavaScript, and other languages**



**Multi-Language – Translation and multilingual queries**



**Creative Writing – Stories, articles, summaries**



**Ethics \& Safety – Responsible AI and compliance scenarios**



**Structured Data – JSON output and formatting tasks**



**🚀 Quick Start**



**Plug in your NVIDIA API key.**



**Choose or add prompts in the script.**



**Run and observe how the GPT-OSS model responds.**





