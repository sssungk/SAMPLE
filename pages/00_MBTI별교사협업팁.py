import streamlit as st

st.set_page_config(page_title="👩‍🏫 교사용 MBTI 협업 가이드", page_icon="📘", layout="centered")

st.title("👩‍🏫 교사용 MBTI 협업 궁합 가이드")
st.markdown("### 당신의 **MBTI 유형**을 선택해보세요 👇")

mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

selected_mbti = st.selectbox("MBTI 선택", mbti_types)

mbti_data = {
    "INTJ": {
        "성향": "📐 전략적 사고, 독립적, 미래 계획을 잘 세우는 유형",
        "궁합": "ENFP, ENTP와 잘 맞아요 🔄",
        "협업팁": "너무 완벽주의적으로 가지 말고, 감정적 반응도 존중해보세요 🌱",
        "효과": "snow"
    },
    "INTP": {
        "성향": "🧠 아이디어 뱅크, 분석적, 이론에 강한 유형",
        "궁합": "ENTJ, ENFP와 잘 어울려요 ⚡",
        "협업팁": "실행력 있는 파트너와 조화롭게 일하면 시너지가 납니다 🔧",
        "효과": "toast"
    },
    "ENTJ": {
        "성향": "🏗 빠른 판단, 추진력 있는 리더",
        "궁합": "INTP, ISFP와 좋은 팀이 돼요 🧩",
        "협업팁": "동료 의견에 더 귀 기울이면 더욱 빛나는 리더십이 됩니다 💬",
        "효과": "success"
    },
    "ENTP": {
        "성향": "🎢 창의적이고 변화를 좋아하는 혁신가",
        "궁합": "INFJ, ISTJ와 잘 맞아요 🔀",
        "협업팁": "아이디어는 풍부하지만, 마무리는 확실히 해야 해요 📌",
        "효과": "toast"
    },
    "INFJ": {
        "성향": "🌌 깊은 공감, 조용한 비전 설계자",
        "궁합": "ENTP, ESTP와 조화를 이룹니다 🌠",
        "협업팁": "감정 소모가 크다면 혼자만 고민하지 마세요 🙏",
        "효과": "snow"
    },
    "INFP": {
        "성향": "🎨 이상주의자, 가치 중심, 감수성이 풍부",
        "궁합": "ENFJ, ISTJ와 찰떡궁합 🎯",
        "협업팁": "갈등을 회피하지 말고, 표현하는 연습도 필요해요 💌",
        "효과": "info"
    },
    "ENFJ": {
        "성향": "🫂 따뜻한 리더, 관계 중심 소통 전문가",
        "궁합": "INFP, ISTP와 환상의 호흡 💖",
        "협업팁": "모두를 배려하다 지치지 않도록, 자기 경계도 지켜주세요 🛡",
        "효과": "success"
    },
    "ENFP": {
        "성향": "🔥 즉흥적이지만 열정 넘치는 에너지 메이커",
        "궁합": "INTJ, ISTJ와 잘 어울려요 🎭",
        "협업팁": "계획적인 파트너와 함께하면 폭발적인 시너지가 💥",
        "효과": "toast"
    },
    "ISTJ": {
        "성향": "📋 꼼꼼하고 책임감 있는 실무형 관리자",
        "궁합": "ENFP, INFP와 균형 잡힌 팀이 돼요 ⚖️",
        "협업팁": "가끔은 융통성도 필요하다는 걸 기억해요 🌀",
        "효과": "info"
    },
    "ISFJ": {
        "성향": "🧸 따뜻하고 조용한 헌신가",
        "궁합": "ESTP, ENTP와 잘 맞아요 🎈",
        "협업팁": "마음속 감사와 의견도 표현해보세요 💭",
        "효과": "snow"
    },
    "ESTJ": {
        "성향": "📊 실용적이고 명확한 리더",
        "궁합": "INFP, ISFP와 잘 맞아요 🔧🎨",
        "협업팁": "자신의 방식만 고집하지 않도록 유연하게 🧘",
        "효과": "success"
    },
    "ESFJ": {
        "성향": "💬 소통능력 탁월, 모두를 챙기는 사람",
        "궁합": "INTP, ISTP와 균형을 이룹니다 🔄",
        "협업팁": "이견도 존중받아야 해요. 갈등 회피보단 정중한 표현을 🌷",
        "효과": "toast"
    },
    "ISTP": {
        "성향": "🔍 조용한 문제 해결사",
        "궁합": "ENFJ, ESFJ와 조화롭습니다 ⚙️",
        "협업팁": "감정 표현을 조금만 더! 👍",
        "효과": "info"
    },
    "ISFP": {
        "성향": "🎼 감성적이고 유연한 예술가",
        "궁합": "ENTJ, ESTJ와 잘 맞아요 🎯",
        "협업팁": "자신의 의견을 묵히지 말고 공유해보세요 💡",
        "효과": "snow"
    },
    "ESTP": {
        "성향": "🏃 활동적이고 실행력 있는 실천가",
        "궁합": "INFJ, ISFJ와 시너지 폭발 💣",
        "협업팁": "긴 회의엔 집중 전략 필요! 💪",
        "효과": "success"
    },
    "ESFP": {
        "성향": "🎉 분위기 메이커, 모두를 웃게 만드는 퍼포머",
        "궁합": "INTJ, ISTJ와 좋은 조화를 이루어요 🎇",
        "협업팁": "즉흥성도 좋지만, 세부 계획은 파트너와 조율해요 📅",
        "효과": "toast"
    }
}

if selected_mbti:
    st.markdown("## 🧩 분석 결과")
    data = mbti_data[selected_mbti]
    
    st.markdown(f"### 🔍 성향")
    st.success(data["성향"])
    
    st.markdown(f"### 🤝 잘 맞는 MBTI")
    st.info(data["궁합"])
    
    st.markdown(f"### 💡 협업 팁")
    st.warning(data["협업팁"])

    # 효과 적용
    effect = data.get("효과")
    if effect == "snow":
        st.snow()
    elif effect == "toast":
        st.toast("분석 완료! 🎉", icon="✨")
    elif effect == "success":
        st.success("완료되었습니다! ✅")
    elif effect == "info":
        st.info("유형 정보가 표시되었습니다! 📘")
