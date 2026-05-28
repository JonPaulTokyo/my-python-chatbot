
# my-python-chatbot 🤖

A lightning-fast, intelligent conversational agent built with Python and powered by **Groq** and Meta's **Llama 3.1** model. 

Created and maintained by [@JonPaulTokyo](https://github.com/JonPaulTokyo).

---

## 🌟 Features

* **Blazing Fast AI:** Utilizes the Groq API for ultra-low latency and near-instant response times.
* **Llama 3.1 Engine:** Runs on Meta's highly capable `llama-3.1-8b-instant` model (with simple code tweaks to swap to Mixtral or others).
* **Context-Aware:** Maintains a running chat history so the bot remembers the context of your conversation.
* **Lightweight & Clean:** Built entirely in Python with minimal dependencies and built-in error handling.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.8** or higher
* A valid **Groq API Key** (You can generate one for free at the [Groq Console](https://console.groq.com/keys))

---

## 🚀 Installation

**1. Clone the repository**
`git clone https://github.com/JonPaulTokyo/my-python-chatbot.git`
`cd my-python-chatbot`

**2. Create a virtual environment (Recommended)**
`python -m venv venv`
`source venv/bin/activate` *(On Windows use: `venv\Scripts\activate`)*

**3. Install dependencies**
For this script, you only need the official Groq Python library:
`pip install groq`

---

## ⚙️ Configuration

To connect the chatbot to the Groq servers, you need to set your API key as an environment variable in your terminal before running the script.

* **Mac/Linux users:**
  `export GROQ_API_KEY="your_actual_api_key_here"`

* **Windows users:**
  `set GROQ_API_KEY=your_actual_api_key_here`

*(Note: For a more permanent local setup, you can install the `python-dotenv` library and use a `.env` file, or paste your key directly into the script for quick local testing only. Never upload your actual API key to GitHub!)*

---

## 💻 Usage

To start the chatbot, simply run the Python script from your terminal:

`python "Chatbot - TB.py"`

Once initialized, type your message in the terminal and press `Enter` to chat with the AI. Type `quit` or `exit` to end the conversation and shut down the bot.

---

## 🛠️ Built With

* [Python](https://www.python.org/) - The programming language used
* [Groq](https://groq.com/) - The ultra-fast AI inference engine
* [Llama 3](https://llama.meta.com/) - The open-source LLM powering the responses

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
Feel free to check the [issues page](https://github.com/JonPaulTokyo/my-python-chatbot/issues) if you want to contribute.

---

## 👨‍💻 Author

**JonPaulTokyo**

* GitHub: [@JonPaulTokyo](https://github.com/JonPaulTokyo)

---

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.
