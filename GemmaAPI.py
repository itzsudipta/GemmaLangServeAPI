from fastapi import FastAPI
from langserve import add_routes
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFacePipeline
from huggingface_hub import login
from fastapi.middleware.cors import CORSMiddleware
import nest_asyncio
import torch
import threading
from pyngrok import ngrok
from langchain_core.tracers import ConsoleCallbackHandler

# Fix asyncio compatibility in Colab
nest_asyncio.apply()

# Hugging Face login
login()

# Load model and tokenizer
model_id = "google/gemma-2b"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map={"": "cpu"}
)

# Create generation pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=256,
    do_sample=True,
    temperature=0.7,
)

# FastAPI app setup
app = FastAPI(
    title="My LangChain Server",
    description="LangChain server for code explanation",
    version="1.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# LangChain setup
llm = HuggingFacePipeline(pipeline=generator)
prompt = ChatPromptTemplate.from_template(
    "Please explain what the following Python function does:\n\n{code}\n\nExplanation:"
)
parser = StrOutputParser()

# Full chain with trace logging
chain = prompt | llm | parser

# Example call for testing with trace logs in console
# (Remove or comment out if not needed in production)
test_input = {"code": "def add(a, b): return a + b"}
print("🔍 Running test chain invocation for debugging:")
print(chain.invoke(test_input, config={"callbacks": [ConsoleCallbackHandler()]}))

# Add LangServe route
add_routes(app, chain, path="/explain")

# Start server with ngrok
PORT = 8002
ngrok.set_auth_token("2vM0B4m36n5BdVFgIXqOPmS1Rsb_47BYD7LzfGdBGttGXTwY6")  # Replace with your token
public_url = ngrok.connect(PORT, bind_tls=True)
print(f"🔗 Public URL: {public_url}/docs")

# Run the server
def run():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)

threading.Thread(target=run, daemon=True).start()
