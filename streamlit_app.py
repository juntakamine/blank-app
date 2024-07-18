import streamlit as st
form langchain.chat_models import ChatOpenAi
form langchain.schema import (SystemMessage, HumanMessage, AIMessage)
def main():
     llm = ChatOpenAI(temperature=0)

st.set_page_config(page_title="My Great ChatGPT,
Page_icon="★"
)
st.header("My Great ChatGPT ★")

if user_input :=st.chat_input("聞きたい事を入力してね")
#何か入力されればここが実行される
