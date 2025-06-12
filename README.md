# 🚀 GemmaLangServeAPI

**GemmaLangServeAPI** is a FastAPI-powered API service built using **Google's Gemma 2B LLM** integrated through **LangChain** and **LangServe**. It allows users to submit Python code and receive human-like explanations in response — ideal for educational, debugging, or AI-assistance use cases.

Hosted via **ngrok** for easy sharing and accessible testing through **Postman**.

---

## 📌 Features

- 🧠 Explains Python functions in natural language
- 🔗 Easily deployable via FastAPI + LangServe
- ⚡ Supports Hugging Face Gemma 2B model pipeline
- 🧪 API testing-ready via Postman or Swagger UI
- ☁️ Hosted via Google Colab with public URL through ngrok

---

## 🛠️ Tech Stack

| Layer               | Technology / Tool                                                                 |
|---------------------|----------------------------------------------------------------------------------|
| **API Framework**   | [FastAPI](https://fastapi.tiangolo.com/)                                          |
| **LLM**             | [Gemma 2B](https://huggingface.co/google/gemma-2b) by Google                      |
| **Model Pipeline**  | [HuggingFace Transformers](https://huggingface.co/transformers)                   |
| **Orchestration**   | [LangChain](https://www.langchain.com/) + [LangServe](https://docs.langchain.com/) |
| **Serving**         | [Uvicorn](https://www.uvicorn.org/)                                               |
| **Tunneling**       | [ngrok](https://ngrok.com/)                                                       |
| **LLM Wrapper**     | [HuggingFacePipeline](https://api.python.langchain.com/en/latest/huggingface.html)|
| **Test Tool**       | [Postman](https://www.postman.com/)                                               |
| **Platform**        | [Google Colab](https://colab.research.google.com/)                                |

---

## 🚀 How to Run

### 🧱 Prerequisites

Install dependencies:

```bash
pip install fastapi uvicorn transformers langchain langserve langchain_huggingface huggingface_hub pyngrok nest_asyncio
```

### ▶️ Run the Server

```bash
python app.py
```

You’ll get a public URL via ngrok, like:

```
🔗 https://your-subdomain.ngrok-free.app/docs
```

Open the `/docs` route to explore Swagger UI or test it using Postman.

---

## 📮 Postman API Guide

| Method | Endpoint   | Description                        |
|--------|------------|------------------------------------|
| POST   | /explain   | Submit Python code for explanation |

### 🧾 Headers

```
Content-Type: application/json
```

### 📤 Request Body

```json
{
  "code": "def add(a, b): return a + b"
}
```

### ✅ Example Response

```json
{
  "output": "This function takes two parameters and returns their sum."
}
```

---

## 🧩 Project Structure

```
GemmaLangServeAPI/
├── app.py            # FastAPI + LangChain setup
├── requirements.txt  # All dependencies
└── README.md         # You're reading it!
```

---

## 📚 Use Cases

- 👨‍💻 Educational tools or tutorials
- 🧠 AI-powered code explanation service
- 🤖 Backend service for developer assistance tools

---

## 📝 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

- 🤖 Google AI – Gemma LLM
- 🧱 LangChain
- 🤗 Hugging Face
- ⚡ FastAPI
