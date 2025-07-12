from langchain_community.llms import HuggingFaceHub
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()
# Set required environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
# Set Hugging Face API key (you can also move this to .env)
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please respond to the user queries."),
    ("user", "Question: {question}")
])

# Streamlit interface
st.title('ChatBot')
input_text = st.text_input("Search")

# Define LLM from HuggingFace
llm =  HuggingFaceEndpoint(
    repo_id="mistralai/Devstral-Small-2507",
    provider="auto",
    temperature=0.7,
    max_new_tokens=512,
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Trigger response
if input_text:
    response = chain.invoke({'question': input_text})
    st.write(response)
