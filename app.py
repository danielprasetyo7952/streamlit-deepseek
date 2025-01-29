import func as f
import streamlit as st

st.set_page_config(page_title="Deepseek-R1 Chatbot", page_icon="🤖", layout="centered")
st.title("Deepseek-R1 Chatbot")
# st.markdown("Welcome to the Deepseek-R1 Chatbot! Feel free to ask me anything. I can help you with a variety of topics, so don't hesitate to start a conversation. Just type your message in the chat box below, and I'll do my best to provide a helpful response.")
# st.markdown("Let's get started!")
st.markdown("---")

# Initialize the messages
if "messages" not in st.session_state:
    st.session_state.messages = []
    
# Display the chat messages history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chatbot interface
if prompt := st.chat_input():
    # Display the user message
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Add the user message to the chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Get the chatbot response
    response = f.chat_response(prompt)
    with st.chat_message("assistant"):
       st.write_stream(f.response_generator(response))
        
    # Add the chatbot response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": response})