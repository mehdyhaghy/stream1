import openai
import streamlit as st
from streamlit_chat import message



openai.api_key = st.secrets["OPENAI_API_KEY"]

styl = f"""
<style>
    .stTextInput {{
      position: fixed;
      bottom: 3rem;
    }}
</style>
"""
st.markdown(styl, unsafe_allow_html=True)

# Prompt
template1 = """Answer the question based on the context below. 
Context: 
As a Tax Resolution Expert ChatBot in the United States provide 
I. Introduction A. What is a Tax Resolution Expert B. Description of Services Offered
II. The Tax Resolution Process A. Step 1: Determine State of Residence, Marital Status, and Amount Owed to IRS and State B. Step 2: Learn About Relevant Information and Forms for Tax Resolution 
III. suggest related forms from IRS for tax resolution.
IV. Conclusion A. Recap of Services Offered B. Call to Action for Those Needing Further Assistance: suggest calling (312)-914-7211
"""


if 'conversation' not in st.session_state:
    st.session_state.conversation = []

st.session_state.conversation.append({"role": "assistant", "content": template1})


def chat_with_bot(message):
    st.session_state.conversation.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.conversation,
        temperature=0.1
    )
    assistant_response = response.choices[0].message['content']
    st.session_state.conversation.append({"role": "assistant", "content": assistant_response})
                                          
st.title("CPA Chatbot")

def get_text():
    input_text = st.text_input("You:", "", key="input")
    return input_text

user_input = get_text()
send_button = st.button("Send")

if send_button and user_input:
    chat_with_bot(user_input)

if st.session_state.conversation:
    for i, msg in enumerate(st.session_state.conversation):
        if msg['role'] == 'user':
            message(msg['content'], is_user=True, key=str(i))
        elif msg['role'] == 'assistant':
            message(msg['content'], key=str(i))
