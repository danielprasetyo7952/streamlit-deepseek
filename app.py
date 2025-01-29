import func as f
import streamlit as st

st.title("Deepseek-R1 Chatbot")

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
    with st.chat_message("assistant"):
       response = st.write_stream(f.chat_response(prompt))
        
    # Add the chatbot response to the chat history
    st.session_state.messages.append({"role": "assistant", "content": response})