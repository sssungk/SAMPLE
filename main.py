import streamlit as st

# 🎨 앱 타이틀
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧠")

st.title("🧠 MBTI 기반 직업 추천기")
st.subheader("당신의 MBTI를 입력하면, 찰떡같은 직업을 추천해드려요! 💼✨")

# 📩 사용자 입력 받기
mbti_input = st.text_input("👉 MBTI를 입력해주세요 (예: INFP, ESTJ 등)", max_chars=4).upper()

# 🎯 MBTI - 직업 매핑
mbti_jobs = {
    "INTJ": ["전략기획가 🧠", "데이터 사이언티스트 📊", "UX 디자이너 🎨"],
    "INFP": ["작가 ✍️", "심리상담사 🧘", "예술가 🎭"],
    "ENTP": ["기획자 📋", "스타트업 CEO 🚀", "마케터 📣"],
    "ESFP": ["배우 🎬", "이벤트 플래너 🎉", "SNS 인플루언서 🤳"],
    "ISTJ": ["회계사 🧾", "공무원 🏛️", "보안 전문가 🛡️"],
    "ENFP": ["크리에이터 🎥", "강연자 🎤", "광고 기획자 🧠"],
    "ISFJ": ["간호사 🏥", "초등 교사 🍎", "도서관 사서 📚"],
    "ESTP": ["영업사원 💼", "구조대원 🚑", "프로 운동선수 🏋️"],
    # ... 더 추가 가능
}

# ✅ 입력 검증 및 추천
if mbti_input:
    if mbti_input in mbti_jobs:
        st.success(f"🎉 {mbti_input}에게 어울리는 직업들입니다!")
        for job in mbti_jobs[mbti_input]:
            st.markdown(f"- {job}")

        # 🎈 풍선 터트리기
        st.balloons()
    else:
        st.error("⚠️ 올바른 MBTI를 입력해주세요! (예: INFP, ENTJ)")
