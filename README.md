# ChatbotHuggingFace

```
# 🤖 Hugging Face Chatbot (LangChain + Streamlit)

A simple GenAI-powered chatbot built using Hugging Face models, LangChain, and deployed on [Render](https://render.com).

## 🔗 Live 
🌍 [Click here to try it live](https://chatbothuggingface.onrender.com/)

---

## 📁 Project Structure

```

chatbot/
├── bot.py                # Main Streamlit app (or replace with your file)
├── requirements.txt      # Python dependencies
├── .env                  # (Used locally, not pushed to GitHub)
└── README.md

````

---

## 🚀 Features

- Chatbot using Hugging Face LLMs (via `langchain`)
- Streamlit UI for interactive chat
- LangChain integration (optional tracing support)
- Deployed on Render (Free tier)
- Supports environment variable-based API key management

---

## 🛠️ Setup (Local)

### 1. Clone the repo
```bash
git clone https://github.com/Pathaan/ChatbotHuggingFace.git
cd ChatbotHuggingFace
````

### 2. Create and activate a virtual environment

```bash
python -m venv myenv
source: myenv\Scripts\activate     # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your `.env` file

Create a `.env` file in the root with:

```
HUGGINGFACEHUB_API_TOKEN=your_token_here
LANGCHAIN_API_KEY=your_langchain_key
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## ☁️ Deployment on Render

### 🔐 Add Environment Variables:

In the Render dashboard, set the following under "Environment Variables":

| Variable                   | Description                       |
| -------------------------- | --------------------------------- |
| `HUGGINGFACEHUB_API_TOKEN` | Your Hugging Face API token       |
| `LANGCHAIN_API_KEY`        | Your LangChain API key (optional) |
| `LANGCHAIN_TRACING_V2`     | Set to `true` to enable tracing   |



## 📦 Requirements

* `streamlit`
* `langchain`
* `transformers`
* `python-dotenv`
* `langchain_community`
* `langchain-huggingface`
* `huggingface_hub`
All specified in `requirements.txt`.

---

## 🙌 Acknowledgements

* [Hugging Face](https://huggingface.co/)
* [LangChain](https://www.langchain.com/)
* [Render](https://render.com/)
* [Streamlit](https://streamlit.io/)

---

## 📬 Contact

**Created by Md Shahrukh (https://github.com/Pathaan)**
Any queries, reach out via [(https://www.linkedin.com/in/md-shahrukh-locky/)]

