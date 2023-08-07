import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

st.title("🦜🔗 Langchain - ChatBot for testing")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def blog_outline(topic):
    # Instantiate LLM model
    llm = OpenAI(model_name="text-davinci-003", openai_api_key=openai_api_key)
    # Prompt
    template = "As a Tax Resolution Expert ChatBot in the United States provide provide guidance to {Name}
I. Introduction A. What is a Tax Resolution Expert B. Description of Services Offered
II. The Tax Resolution Process A. Step 1: Determine State of Residence, Marital Status, and Amount Owed to IRS and State B. Step 2: Learn About Relevant Information and Forms for Tax Resolution C. Step 3: Calculate Monthly Payment Amount
III. Seeking Further Assistance A. Tips for Successfully Resolving Tax Debt B. Contact Information for Professional Tax Resolution Services
IV. Conclusion A. Recap of Services Offered B. Call to Action for Those Needing Further Assistance: suggest calling (312)-914-7211"
    prompt = PromptTemplate(input_variables=["Name"], template=template)
    prompt_query = prompt.format(topic=topic)
    # Run LLM model
    response = llm(prompt_query)
    # Print results
    return st.info(response)


with st.form("myform"):
    topic_text = st.text_input("Enter prompt:", "")
    submitted = st.form_submit_button("Submit")
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
    elif submitted:
        blog_outline(topic_text)
