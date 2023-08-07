import openai
import streamlit as st
from langchain.chains import ConversationChain
from langchain.llms import OpenAI
from langchain import PromptTemplate

openai.api_key = st.secrets["OPENAI_API_KEY"]
openai_api_key= st.secrets["OPENAI_API_KEY"]

def generate_response(topic):
  llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key)
  # Prompt
  template = """Answer the question based on the context below. If the
question cannot be answered using the information provided answer
with "Please call (312)xxxxxx for more assistance".
Context: 
As a Tax Resolution Expert ChatBot in the United States provide 
I. Introduction A. What is a Tax Resolution Expert B. Description of Services Offered
II. The Tax Resolution Process A. Step 1: Determine State of Residence, Marital Status, and Amount Owed to IRS and State B. Step 2: Learn About Relevant Information and Forms for Tax Resolution 
III. Seeking Further Assistance A. Tips for Successfully Resolving Tax Debt B. Contact Information for Professional Tax Resolution Services
IV. Conclusion A. Recap of Services Offered B. Call to Action for Those Needing Further Assistance: suggest calling (312)-914-7211
Question: {topic}

Answer: """
  prompt = PromptTemplate(input_variables=['topic'], template=template)
  prompt_query = prompt.format(topic=topic)
  # Run LLM model and print out response
  response = llm(prompt_query)
  return st.info(response)



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
    msg = generate_response(prompt)
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
