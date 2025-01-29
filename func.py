import ollama
import streamlit as st
import time

MODEL = "deepseek-r1:7b"

try:
    ollama.chat(MODEL)
except ollama.ResponseError as e:
    st.error(f"Model '{MODEL}' not found. Pulling model...")
    if e.status_code == 404:
        ollama.pull(MODEL)

def response_generator(message_content: str):
    """
    Generates a response by yielding words from the input message content with a delay between each word.

    Args:
        message_content (str): The input message content to be processed.

    Yields:
        str: Each word from the message content followed by a space, and a newline character at the end of each line.
    """
    for line in message_content.splitlines():
        for word in line.split():
            yield word + " "
            time.sleep(0.05)
        yield "\n"

def chat_response(prompt: str) -> str:
    """
    Generates a chat response based on the given prompt using the Ollama function.
    Args:
        prompt (str): The input prompt to generate a response for.
    Returns:
        str: The generated response. If the response message is None, returns a default apology message.
             If the response contains "<think>" and "</think>" tags, they are removed from the content.
    """
    response: ollama.ChatResponse = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt,
            },
        ],
    )
    
    if response.message is None:
        return "I'm sorry, I don't have a response for that."
    
    if "<think>" and "</think>" in response.message.content:
        response.message.content = response.message.content.replace("<think>", "").replace("</think>", "")
    
    return response.message.content
