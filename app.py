import streamlit as st

st.set_page_config(page_title="AI 챗봇", page_icon="🤖")

st.title("🤖 간단한 AI 챗봇")

# 세션 상태에 대화 기록 저장
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# 대화 기록 표시
for msg in st.session_state["messages"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 사용자 입력 받기
user_input = st.chat_input("메시지를 입력하세요...")

# 간단한 응답 생성 함수 (패턴 매칭 또는 고정 응답)
def generate_response(user_message):
    user_message = user_message.lower()
    if "안녕" in user_message:
        return "안녕하세요! 무엇을 도와드릴까요?"
    elif "이름" in user_message:
        return "저는 간단한 AI 챗봇입니다."
    elif "고마워" in user_message:
        return "천만에요!"
    else:
        return "죄송해요, 아직 그 질문에는 답변할 수 없어요."

# 입력이 있으면 대화 기록에 추가 및 응답 생성
if user_input:
    st.session_state["messages"].append({"role": "user", "content": user_input})
    response = generate_response(user_input)
    st.session_state["messages"].append({"role": "assistant", "content": response})
    st.experimental_rerun()  # 새 메시지 바로 반영 