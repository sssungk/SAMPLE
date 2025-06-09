import streamlit as st

# 🎨 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧠")

st.title("🧠 MBTI 기반 직업 추천기")
st.subheader("당신의 MBTI를 선택해보세요! 찰떡같은 직업을 추천해드릴게요 💼✨")

# 📌 MBTI 구성 요소
ie = st.selectbox("1️⃣ 에너지 방향", ["I (내향)", "E (외향)"])
ns = st.selectbox("2️⃣ 인식 방식", ["N (직관)", "S (감각)"])
ft = st.selectbox("3️⃣ 판단 기준", ["F (감정)", "T (사고)"])
jp = st.selectbox("4️⃣ 생활 양식", ["J (판단)", "P (인식)"])

# 🧩 조합 만들기
mbti_input = (
    ie[0] + ns[0] + ft[0] + jp[0]
)  # 예: I + N + F + P → INFP

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
    # 필요한 만큼 추가 가능
}

# ✅ 추천 결과
if mbti_input:
    st.markdown(f"## 🧬 당신의 MBTI: **{mbti_input}**")

    if mbti_input in mbti_jobs:
        st.success(f"🎯 {mbti_input}에게 어울리는 직업은 다음과 같아요!")
        for job in mbti_jobs[mbti_input]:
            st.markdown(f"- {job}")

        st.balloons()  # 🎈 빵야!
    else:
        st.warning("해당 MBTI의 직업 정보가 아직 준비되지 않았어요 🙏")
