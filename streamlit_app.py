import streamlit as st
from langchain_community.llms import OpenAI

st.title('🦜🔗 Quickstart App')

openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
model_version = st.sidebar.selectbox('Select Model Version', ['gpt-3.5-turbo', 'gpt-4'])

def generate_response(input_text):
    if openai_api_key.startswith('sk-'):
        llm = OpenAI(model_name=model_version, temperature=0.7, openai_api_key=openai_api_key)
        response = llm(input_text)
        st.info(response)
    else:
        st.warning('Invalid OpenAI API key!', icon='⚠')

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
