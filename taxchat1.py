import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

with st.sidebar:
    customer_name = st.text_input("Name", key="customer_name")
    customer_phone = st.text_input("Phone", key="customer_phone")
    customer_email = st.text_input("Email", key="customer_email")
    "[Get an help from a human](https://www.google.com/)"
    

st.title("💬 CPA Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hi, I'm a Tax resolution AI bot , How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
