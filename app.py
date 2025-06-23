import streamlit as st
import openai
import os

st.set_page_config(page_title="AI 챗봇", page_icon="🤖")

st.title("🤖 GPT 기반 AI 챗봇")

# 1. API 키 입력창
api_key = st.text_input(
    "OpenAI API 키를 입력하세요 (sk-로 시작)",
    type="password",
    value=st.session_state.get("api_key", "")
)
if api_key:
    st.session_state["api_key"] = api_key

# 2. API 키가 없으면 안내 메시지
if "api_key" not in st.session_state or not st.session_state["api_key"]:
    st.info("먼저 OpenAI API 키를 입력해야 챗봇을 사용할 수 있습니다.")
    st.stop()

# 최신 openai 방식: 클라이언트 객체 생성
client = openai.OpenAI(api_key=st.session_state["api_key"])

# 3. 대화 세션 관리
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
    response = client.chat.completions.create(
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