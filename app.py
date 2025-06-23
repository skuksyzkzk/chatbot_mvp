import streamlit as st
import openai
import os

st.set_page_config(page_title="AI 챗봇", page_icon="🤖")

st.title("🤖 GPT 기반 AI 챗봇")

# OpenAI API 키 입력 (보안상 환경변수 사용 권장)
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

# 세션 상태에 대화 기록 저장
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 대화 기록 표시
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력 받기
user_input = st.chat_input("메시지를 입력하세요...")

def generate_response(messages):
    # OpenAI Chat API 호출
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 또는 gpt-4
        messages=messages
    )
    return response.choices[0].message.content

# 입력이 있으면 대화 기록에 추가 및 응답 생성
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    # OpenAI API에 전체 대화 내역 전달
    response = generate_response([
        {"role": m["role"], "content": m["content"]} for m in st.session_state["messages"]
    ])
    st.session_state["messages"].append({"role": "assistant", "content": response}) 