import func as f
import streamlit as st

st.title("Deepseek-R1 Chatbot")
prompt = st.text_area("Message", height=100, placeholder="Type a message")
send = st.button("Send")
st.markdown("## Response:")

if send:
    response = f.chat_response(prompt)
    st.markdown("---")
    st.markdown(response)
    st.markdown("---")