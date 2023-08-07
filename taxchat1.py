import openai
import streamlit as st

st.title("CPA Chat")

openai.api_key = st.secrets["OPENAI_API_KEY"]

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
prompt="""As a Tax Resolution Expert ChatBot in the United States provide 
I. Introduction A. What is a Tax Resolution Expert B. Description of Services Offered
II. The Tax Resolution Process A. Step 1: Determine State of Residence, Marital Status, and Amount Owed to IRS and State B. Step 2: Learn About Relevant Information and Forms for Tax Resolution C. Step 3: Calculate Monthly Payment Amount
III. Seeking Further Assistance A. Tips for Successfully Resolving Tax Debt B. Contact Information for Professional Tax Resolution Services
IV. Conclusion A. Recap of Services Offered B. Call to Action for Those Needing Further Assistance: suggest calling (312)-914-7211 """
st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you with your tax resolution questions?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    #st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
