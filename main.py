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
    "INTP": ["이론 물리학자 🔬", "시스템 엔지니어 💻", "AI 연구원 🤖"],
    "ENTJ": ["CEO 💼", "비즈니스 컨설턴트 📈", "프로젝트 매니저 🗂️"],
    "ENTP": ["기획자 📋", "스타트업 창업가 🚀", "브랜드 마케터 📣"],

    "INFJ": ["상담사 🧘", "작가 ✍️", "교육 콘텐츠 개발자 🎓"],
    "INFP": ["시인 ✒️", "일러스트레이터 🖌️", "예술가 🎭"],
    "ENFJ": ["리더십 트레이너 🗣️", "교사 🍎", "사회복지사 ❤️"],
    "ENFP": ["유튜버 🎥", "동기부여 연설가 🎤", "콘텐츠 마케터 🧠"],

    "ISTJ": ["회계사 🧾", "공무원 🏛️", "군인 🪖"],
    "ISFJ": ["간호사 🏥", "초등학교 교사 👩‍🏫", "도서관 사서 📚"],
    "ESTJ": ["경영 관리자 📂", "경찰관 🚓", "생산 관리자 🏭"],
    "ESFJ": ["병원 행정직 🏥", "고객 서비스 매니저 📞", "이벤트 코디네이터 🎊"],

    "ISTP": ["기계 엔지니어 🔧", "드론 조종사 🚁", "자동차 정비사 🚗"],
    "ISFP": ["패션 디자이너 👗", "플로리스트 🌸", "사진작가 📷"],
    "ESTP": ["세일즈 전문가 💼", "소방관 🚒", "스턴트 배우 🎬"],
    "ESFP": ["무대 배우 🎭", "파티 플래너 🎉", "SNS 인플루언서 🤳"],
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
