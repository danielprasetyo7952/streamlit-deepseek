import streamlit as st
import time
from ollama import chat, pull
from ollama import ChatResponse, ResponseError

MODEL = "deepseek-r1:1.5b"

try:
    chat(MODEL)
except ResponseError as e:
    st.error(f"Model '{MODEL}' not found. Pulling model...")
    if e.status_code == 404:
        pull(MODEL)

def chat_response(prompt: str):
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
    
    for line in clean_response.splitlines(keepends=True):
        for word in line.split():
            yield word + " "
            time.sleep(0.05)
        # Yield a newline character to preserve the original formatting
        if line.endswith("\n"):
            yield "\n"
