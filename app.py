import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

st.set_page_config(page_title="ChatterBot 챗봇", page_icon="🤖")
st.title("🤖 ChatterBot 기반 챗봇 (무료)")

# 챗봇 객체를 세션에 저장 (최초 1회만 학습)
if "chatbot" not in st.session_state:
    chatbot = ChatBot("MyBot", read_only=True)
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train("chatterbot.corpus.english")  # 영어 코퍼스 학습
    st.session_state["chatbot"] = chatbot

if "messages" not in st.session_state:
    st.session_state["messages"] = []

for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("메시지를 입력하세요... (영어 권장)")

if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    response = st.session_state["chatbot"].get_response(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": str(response)}) 