import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

# --- 페이지 기본 설정 ----
st.set_page_config(
    page_title="통합허브 개발 주소(룰루랄라한기쌤) - 마음 공부 포털",
    page_icon="👋",
    layout="wide",
)



# --- Index 탭 ---

st.title("통합허브 개발 주소(룰루랄라한기쌤 개발) - 마음 공부 포털")
st.write(":star: 다양한 교육/마음 관련 사이트를 한 곳에 모았습니다.")
st.write("---")

# 카드 데이터 정의
cards = [
    {
        "title": "나의 gets 모음",
        "desc": "나만의 GPTs 모음집",
        "url": "https://plusiam.github.io/my-gp",
        "button": "바로가기"
    },
    {
        "title": "룰루랄라 한기쌤의 GPTs 모음",
        "desc": "교육용 AI 도구 포트폴리오 (ts-website)",
        "url": "https://plusiam.github.io/my-gp",  # 실제 ts-website 주소로 교체 가능
        "button": "바로가기"
    },
    {
        "title": "사고가시화 툴킷",
        "desc": "생각이 보이는 교실",
        "url": "https://plusiam.github.io/edu-thinking-toolkit/",
        "button": "바로가기"
    },
    {
        "title": "정서조절 웹학습지",
        "desc": "마음허브",
        "url": "https://plusiam.github.io/maum-hub/",
        "button": "바로가기"
    },
    {
        "title": "위드-유 인성놀이터",
        "desc": "마음챙김 인성교육 사이트",
        "url": "https://plusiam.github.io/widyu-mindfulness-website/",
        "button": "바로가기"
    },
    {
        "title": "마음봄 웹사이트",
        "desc": "마음봄 프로젝트 공식 사이트",
        "url": "https://plusiam.github.io/maumbom-website/",
        "button": "바로가기"
    },
    {
        "title": "마음봄 챗봇",
        "desc": "마음봄 AI 챗봇 (ChatGPT)",
        "url": "https://chatgpt.com/g/g-6735399fe05c81908ab27480dd89f233-maeumbom-2025-04-09",
        "button": "바로가기"
    },
    {
        "title": "나도 멋진 친구!",
        "desc": "내 친구의 '색깔'을 찾아주는 비밀 작전! 🌟",
        "url": "https://plusiam.github.io/invisible-child-worksheet/",
        "button": "바로가기"
    },
    # 추가 카드들
    {
        "title": "마음성장 일기",
        "desc": "앱시트 - 구글 드라이브로 자동 저장",
        "url": "https://script.google.com/macros/s/AKfycbwwXqEDmi3d5PiREc0_13ttTgtpiRbTz84Scded9u1DBMggoanW5LXVB3yJCiRmLg_k0w/exec",
        "button": "바로가기"
    },
    {
        "title": "ABC 생각바꾸기",
        "desc": "앱시트 - 구글 드라이브 자동 저장",
        "url": "https://script.google.com/macros/s/AKfycby9qLF-HnLegM7xtwPY3Y_LKtVRLtQWEhsJLGn6F-MBfu0sJjhfkkB_mL3lKrmmdOyOFw/exec",
        "button": "바로가기"
    },
    {
        "title": "ORID Reflection Tool",
        "desc": "ORID 성찰 도구",
        "url": "https://plusiam.github.io/orid-reflection-tool",
        "button": "바로가기"
    },
    {
        "title": "positive-card-maker",
        "desc": "프리미엄 긍정 카드 메이커",
        "url": "https://plusiam.github.io/positive-card-maker",
        "button": "바로가기"
    },
    {
        "title": "positive-card-maker (마음허브)",
        "desc": "프리미엄 긍정 카드 메이커 (마음허브)",
        "url": "https://plusiam.github.io/maum-hub/positive-card-maker/",
        "button": "바로가기"
    },
    {
        "title": "스텝 인 사이드",
        "desc": "Step Inside 워크시트",
        "url": "https://plusiam.github.io/step-inside-worksheet",
        "button": "바로가기"
    },
    {
        "title": "스텝 인 사이드 (개선판)",
        "desc": "Step Inside Improved - 교사용/학생용",
        "url": "https://plusiam.github.io/step-inside-worksheet-improved/teacher.html",
        "button": "교사용"
    },
    {
        "title": "스텝 인 사이드 (개선판)",
        "desc": "Step Inside Improved - 학생용",
        "url": "https://plusiam.github.io/step-inside-worksheet-improved/",
        "button": "학생용"
    },
    {
        "title": "우리 가족, 행복한 순간 그리기 v2",
        "desc": "가족 행복 순간 그리기",
        "url": "https://plusiam.github.io/family-happy-moments-v2/",
        "button": "바로가기"
    },
    {
        "title": "친구 카운셀러",
        "desc": "친구 상담 도구",
        "url": "https://plusiam.github.io/friend-consultation",
        "button": "바로가기"
    },
    {
        "title": "고민 요청하기",
        "desc": "활동 1 : 고민 요청하기",
        "url": "https://plusiam.github.io/help-request-form",
        "button": "바로가기"
    },
    {
        "title": "See-Think-Wonder v2",
        "desc": "사고가시화 - 학생 제공 템플릿(교사용)",
        "url": "https://plusiam.github.io/see-think-wonder-v2",
        "button": "바로가기"
    },
    {
        "title": "See-Think-Wonder Template",
        "desc": "사고가시화 템플릿(교사용)",
        "url": "https://plusiam.github.io/see-think-wonder-templet",
        "button": "바로가기"
    },
    {
        "title": "3-2-1 Bridge",
        "desc": "3-2-1 브릿지 사고 도구",
        "url": "https://plusiam.github.io/3-2-1-bridge",
        "button": "바로가기"
    },
    {
        "title": "Connect-Extend-Challenge Templates",
        "desc": "Connect-Extend-Challenge 템플릿",
        "url": "https://plusiam.github.io/connect-extend-challengge-templates",
        "button": "바로가기"
    },
    {
        "title": "Think-Puzzle-Explore",
        "desc": "사고 퍼즐 탐구 도구",
        "url": "https://plusiam.github.io/think-puzzle-explore",
        "button": "바로가기"
    },
    {
        "title": "Step Inside v2",
        "desc": "Step Inside v2 도구",
        "url": "https://plusiam.github.io/step-inside-v2",
        "button": "바로가기"
    },
    {
        "title": "Generate-Classify-Connect-Elaborate",
        "desc": "생성-분류-연결-확장 도구",
        "url": "https://plusiam.github.io/generate-classify-connect-elaborate",
        "button": "바로가기"
    },
    {
        "title": "Sentence-Phrase-Word",
        "desc": "문장-구-단어 도구",
        "url": "https://plusiam.github.io/sentence-phrase-word",
        "button": "바로가기"
    },
    {
        "title": "Interactive Viewpoints Circle",
        "desc": "관점의 원 도구",
        "url": "https://plusiam.github.io/interactive-viewpoints-circle",
        "button": "바로가기"
    },
    {
        "title": "Visible Thinking Hub",
        "desc": "Visible Thinking 메인 허브",
        "url": "https://plusiam.github.io/visible-thinking-hub",
        "button": "바로가기"
    },
    {
        "title": "전체 도구 목록 및 주소",
        "desc": "See-Think-Wonder, Frayer Model, Headlines 등 전체 도구",
        "url": "https://plusiam.github.io/see-think-wonder-v2/",  # 대표 주소
        "button": "바로가기"
    },
    {
        "title": "Friend Helper",
        "desc": "친구 도우미 도구",
        "url": "https://plusiam.github.io/friend-helper",
        "button": "바로가기"
    },
    {
        "title": "ABC Friend Consultant",
        "desc": "ABC 친구 상담 도구",
        "url": "https://plusiam.github.io/abc-friend-consultant",
        "button": "바로가기"
    },
    {
        "title": "제주 다다익선 워크북",
        "desc": "제주 다다익선 워크북",
        "url": "https://plusiam.github.io/jeju-dadaiksun-workbook",
        "button": "바로가기"
    },
    {
        "title": "ABC Friend Helper",
        "desc": "ABC 친구 도우미",
        "url": "https://plusiam.github.io/abc-friend-helper",
        "button": "바로가기"
    },
    {
        "title": "ABC Friend Helper (Vercel)",
        "desc": "ABC 친구 도우미 (Vercel 배포)",
        "url": "https://abc-friend-helper.vercel.app/",
        "button": "바로가기"
    },
    {
        "title": "ABC Friend Peer",
        "desc": "ABC 친구 피어 도구",
        "url": "https://plusiam.github.io/abc-friend-peer",
        "button": "바로가기"
    },
    {
        "title": "ABC Heart Bridge",
        "desc": "ABC 하트 브릿지",
        "url": "https://plusiam.github.io/abc-heart-bridge",
        "button": "바로가기"
    },
    {
        "title": "ABC Heart Bridge (스마트/고급)",
        "desc": "ABC 하트 브릿지 스마트/고급 버전",
        "url": "https://plusiam.github.io/abc-heart-bridge/index_smart_advanced.html",
        "button": "바로가기"
    },
    {
        "title": "문패 메이커",
        "desc": "문패 만들기 도구",
        "url": "https://plusiam.github.io/munpae-maker",
        "button": "바로가기"
    },
    {
        "title": "Bridge Learning Sheets",
        "desc": "브릿지 학습지",
        "url": "https://plusiam.github.io/bridge-learning-sheets",
        "button": "바로가기"
    },
    {
        "title": "Mood Weather Diary",
        "desc": "기분 날씨 일기",
        "url": "https://plusiam.github.io/mood-weather-diary",
        "button": "바로가기"
    },
    {
        "title": "Friendship Graph Tool",
        "desc": "우정 그래프 도구",
        "url": "https://plusiam.github.io/friendship-graph-tool",
        "button": "바로가기"
    },
    {
        "title": "Emotion 4 Quadrant Explorer",
        "desc": "감정 4분면 탐색기",
        "url": "https://plusiam.github.io/emotion-4quadrant-explorer",
        "button": "바로가기"
    },
    {
        "title": "클로드 아티팩트",
        "desc": "클로드 AI 아티팩트",
        "url": "https://claude.ai/public/artifacts/aa9a0ee5-a739-44a3-a597-43362c23f45e",
        "button": "바로가기"
    },
    {
        "title": "감정 카드 메이커",
        "desc": "감정 카드 메이커",
        "url": "https://plusiam.github.io/emotion-card-maker/",
        "button": "바로가기"
    },
    {
        "title": "버킷 드림즈",
        "desc": "버킷 드림즈",
        "url": "https://plusiam.github.io/bucket-dreams/",
        "button": "바로가기"
    },
    {
        "title": "버킷 리스트",
        "desc": "버킷 리스트",
        "url": "https://plusiam.github.io/bucket-list",
        "button": "바로가기"
    },
]

# 3개씩 한 줄에 카드 배치
for i in range(0, len(cards), 3):
    cols = st.columns(4)
    for j, card in enumerate(cards[i:i+4]):
        with cols[j]:
            with st.container():
                st.markdown(f"""
                    <div style='border:1px solid #eee; border-radius:12px; padding:20px; margin-bottom:10px; background-color:#fafbfc;'>
                        <h4 style='margin-bottom:8px'>{card['title']}</h4>
                        <p style='font-size:15px; color:#555; margin-bottom:16px'>{card['desc']}</p>
                        <a href='{card['url']}' target='_blank' style='text-decoration:none;'>
                            <button style='background:#4F8BF9; color:white; border:none; border-radius:6px; padding:8px 18px; font-size:15px; cursor:pointer;'>{card['button']}</button>
                        </a>
                    </div>
                """, unsafe_allow_html=True)
st.write("---")

