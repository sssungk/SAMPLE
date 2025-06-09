import streamlit as st

st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧠", layout="centered")

st.title("🧠 MBTI 기반 직업 추천 서비스")
st.write("당신의 MBTI 유형에 맞는 추천 직업을 확인해보세요! 🎯")

# 선택형 MBTI 입력
mbti_input = st.selectbox("당신의 MBTI를 선택해주세요:", [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
])

# MBTI 성향 요약
mbti_traits = {
    "INTJ": "독립적이며 전략적인 사고를 하는 혁신가입니다.",
    "INTP": "논리적이고 탐구심이 강한 사색가입니다.",
    "ENTJ": "목표 지향적이며 리더십이 강한 통솔자입니다.",
    "ENTP": "호기심 많고 아이디어가 넘치는 혁신가입니다.",
    "INFJ": "깊은 통찰과 공감을 가진 조용한 이상주의자입니다.",
    "INFP": "감성적이고 창의적인 이상주의자입니다.",
    "ENFJ": "사람들을 이끄는 따뜻한 지도자입니다.",
    "ENFP": "에너지 넘치고 열정적인 자유로운 영혼입니다.",
    "ISTJ": "책임감 강하고 조직적인 관리자입니다.",
    "ISFJ": "헌신적이고 성실한 보호자입니다.",
    "ESTJ": "체계적이고 단호한 리더입니다.",
    "ESFJ": "친절하고 협력적인 사람 중심 관리자입니다.",
    "ISTP": "실용적이고 조용한 문제 해결자입니다.",
    "ISFP": "예술적이고 온화한 감성가입니다.",
    "ESTP": "모험심 많고 사교적인 활동가입니다.",
    "ESFP": "즉흥적이고 매력적인 퍼포머입니다.",
}

# MBTI별 직업 추천 (직업명, 설명, 링크)
mbti_careers_with_links = {
    "INTJ": [
        ("전략기획가 🧠", "체계적이고 미래지향적인 사고를 하는 INTJ에게 잘 맞아요.", "https://www.career.go.kr/cnet/front/base/job/jobView.do?SEQ=172"),
        ("데이터 사이언티스트 📊", "논리적인 성향이 데이터 해석에 강점을 줘요.", "https://www.jobkorea.co.kr/starter/JobTip/View/18914"),
        ("UX 디자이너 🎨", "사용자 중심 사고를 설계적으로 풀어낼 수 있어요.", "https://brunch.co.kr/@uxcolumns")
    ],
    "INTP": [
        ("이론 물리학자 🔬", "복잡한 문제 해결과 창의적 사고에 강해요.", "https://ko.wikipedia.org/wiki/%EB%AC%BC%EB%A6%AC%ED%95%99%EC%9E%90"),
        ("시스템 엔지니어 💻", "논리적 문제 분석에 탁월해요.", "https://career.go.kr/"),
        ("AI 연구원 🤖", "혁신적이고 독창적인 아이디어를 구현해요.", "https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?cbIdx=65914&bcIdx=22924")
    ],
    "ENTJ": [
        ("CEO 💼", "리더십이 강하고 목표 지향적인 성향이에요.", "https://ko.wikipedia.org/wiki/CEO"),
        ("비즈니스 컨설턴트 📈", "전략적 사고와 판단력을 활용할 수 있어요.", "https://www.jobkorea.co.kr/Starter/JobTip/View/17764"),
        ("프로젝트 매니저 🗂️", "자원과 인력을 효율적으로 조율할 수 있어요.", "https://career.go.kr/")
    ],
    "ENTP": [
        ("기획자 📋", "아이디어가 풍부하고 유연한 사고를 가진 성향이에요.", "https://www.jobkorea.co.kr/Starter/JobTip/View/17772"),
        ("스타트업 창업가 🚀", "도전을 즐기고 빠른 판단이 가능해요.", "https://startup.go.kr"),
        ("브랜드 마케터 📣", "창의적인 방향 설정이 가능해요.", "https://brunch.co.kr/@brunchbiz/3")
    ],
    "INFJ": [
        ("상담사 🧘", "깊은 공감 능력과 타인에 대한 이해가 강해요.", "https://www.counseling.or.kr"),
        ("작가 ✍️", "내면 세계를 글로 풀어내는 데 재능이 있어요.", "https://brunch.co.kr"),
        ("교육 콘텐츠 개발자 🎓", "의미 있는 교육을 설계하고 전달할 수 있어요.", "https://career.go.kr")
    ],
    "INFP": [
        ("시인 ✒️", "감성이 풍부하고 내면의 이야기를 표현하는 데 능해요.", "https://ko.wikipedia.org/wiki/%EC%8B%9C"),
        ("일러스트레이터 🖌️", "따뜻한 감성을 시각화할 수 있어요.", "https://career.go.kr"),
        ("예술가 🎭", "자아표현과 개성이 강한 분야에 어울려요.", "https://www.work.go.kr")
    ],
    "ENFJ": [
        ("리더십 트레이너 🗣️", "사람들을 격려하고 성장시키는 데 능해요.", "https://career.go.kr"),
        ("교사 🍎", "타인을 배려하며 가르치는 데 기쁨을 느껴요.", "https://www.edunet.net"),
        ("사회복지사 ❤️", "사회적 가치와 공동체 의식이 중요한 성향이에요.", "https://www.kasw.or.kr")
    ],
    "ENFP": [
        ("유튜버 🎥", "창의적이고 즉흥적인 아이디어로 콘텐츠를 만들기 좋아요.", "https://www.youtube.com/creators/"),
        ("동기부여 연설가 🎤", "사람들에게 영감을 주고 동기를 부여할 수 있어요.", "https://www.ted.com"),
        ("콘텐츠 마케터 🧠", "스토리텔링에 강한 재능을 발휘할 수 있어요.", "https://brunch.co.kr")
    ],
    "ISTJ": [
        ("회계사 🧾", "정확하고 체계적인 업무 스타일에 적합해요.", "https://www.kicpa.or.kr"),
        ("공무원 🏛️", "안정적이고 신뢰받는 환경을 선호해요.", "https://www.gosi.go.kr"),
        ("군인 🪖", "규칙과 질서를 존중하는 성향이에요.", "https://www.mma.go.kr")
    ],
    "ISFJ": [
        ("간호사 🏥", "헌신적이고 타인을 돕는 데 보람을 느껴요.", "https://www.kna.or.kr"),
        ("초등학교 교사 👩‍🏫", "아이들을 돌보는 데 적합해요.", "https://www.edunet.net"),
        ("도서관 사서 📚", "조용히 일하는 환경을 선호해요.", "https://nl.go.kr")
    ],
    "ESTJ": [
        ("경영 관리자 📂", "조직적이고 리더십을 발휘하는 역할에 잘 맞아요.", "https://career.go.kr"),
        ("경찰관 🚓", "정의감과 책임감이 강한 성향이에요.", "https://www.police.go.kr"),
        ("생산 관리자 🏭", "효율성과 체계적인 운영에 강해요.", "https://www.jobkorea.co.kr")
    ],
    "ESFJ": [
        ("병원 행정직 🏥", "타인을 돕고 실용적인 환경에서 일하는 걸 좋아해요.", "https://career.go.kr"),
        ("고객 서비스 매니저 📞", "긍정적인 상호작용에 강해요.", "https://www.jobkorea.co.kr"),
        ("이벤트 코디네이터 🎊", "행사를 조율하는 데 잘 맞아요.", "https://brunch.co.kr")
    ],
    "ISTP": [
        ("기계 엔지니어 🔧", "문제 해결과 도구 사용에 능숙해요.", "https://career.go.kr"),
        ("드론 조종사 🚁", "실용적인 기술력에 강해요.", "https://www.koreadroneschool.co.kr"),
        ("자동차 정비사 🚗", "무언가를 손으로 다루는 걸 선호해요.", "https://www.katech.re.kr")
    ],
    "ISFP": [
        ("패션 디자이너 👗", "감각을 표현하는 데 재능이 있어요.", "https://www.kofoti.or.kr"),
        ("플로리스트 🌸", "자연스럽고 섬세한 감성을 살릴 수 있어요.", "https://florist.or.kr"),
        ("사진작가 📷", "감정을 섬세하게 포착하는 데 적합해요.", "https://www.kpanet.or.kr")
    ],
    "ESTP": [
        ("세일즈 전문가 💼", "에너지 넘치고 말솜씨가 좋아요.", "https://brunch.co.kr"),
        ("소방관 🚒", "위기 대응과 빠른 행동에 능해요.", "https://www.119.go.kr"),
        ("스턴트 배우 🎬", "도전적인 활동에 매력을 느껴요.", "https://www.koreastunt.com")
    ],
    "ESFP": [
        ("무대 배우 🎭", "표현력과 주목받는 걸 즐기는 성향이에요.", "https://theater.seoul.go.kr"),
        ("파티 플래너 🎉", "사람들과 어울리고 축제를 만드는 걸 좋아해요.", "https://www.eventplanner.co.kr"),
        ("SNS 인플루언서 🤳", "외향적이며 트렌드에 민감해요.", "https://creatorlink.net")
    ]
}

# 결과 출력
if mbti_input in mbti_careers_with_links:
    st.subheader(f"📌 {mbti_input} 성향 요약")
    st.info(mbti_traits.get(mbti_input, "성향 정보 없음"))

    st.success(f"🎯 {mbti_input}에게 어울리는 직업과 이유는 다음과 같아요:")

    for job, reason, link in mbti_careers_with_links[mbti_input]:
        st.markdown(f"**{job}**  \n{reason}")
        st.markdown(f"[🔗 자세히 보기]({link})", unsafe_allow_html=True)
        st.markdown("---")

    st.balloons()
else:
    st.warning("해당 MBTI의 정보가 아직 준비되지 않았어요 🙏")
