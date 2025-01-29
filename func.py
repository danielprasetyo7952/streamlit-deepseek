import streamlit as st
from ollama import chat
from ollama import pull
from ollama import ChatResponse
from ollama import ResponseError

MODEL = "deepseek-r1:1.5b"

try:
    chat(MODEL)
except ResponseError as e:
    st.error(f"Model '{MODEL}' not found. Pulling model...")
    if e.status_code == 404:
        pull(MODEL)

def chat_response(prompt: str) -> str:
    response: ChatResponse = chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    
    clean_response = response.message.content.replace("<think>", "")
    clean_response = clean_response.replace("</think>", "")
    
    return clean_response
