import streamlit as st
from PIL import Image

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="안녕하세요! 신송배입니다.",
    page_icon="👋",
    layout="wide",
)
 
# --- 메인 페이지 ---
st.title("안녕하세요, 코딩 어시스턴트 pgconek입니다. 👨‍💻")

# --- 헤더 섹션 ---
with st.container():
    # 컬럼을 사용하여 이미지와 텍스트를 나란히 배치합니다.
    left_column, right_column = st.columns((2, 1))
    with left_column:
        st.subheader("반갑습니다! 저는 신송배입니다.")
        st.write(
            """
            저는 5년 차 백엔드 개발자로, 대용량 트래픽 처리와 안정적인 시스템 구축에 관심이 많습니다.
            새로운 기술을 배우고 동료들과 지식을 공유하는 것을 좋아합니다.
            현재는 AI 기술을 활용한 서비스 개발에 참여하고 있습니다..
            """
        )
        # 링크를 버튼처럼 보이게 만듭니다.
        st.write("[GitHub 프로필 보기 >](https://github.com)")

    with right_column:
        # 이미지를 추가합니다. 'images/profile.png' 경로에 자신의 사진을 넣어보세요.
        # 이미지가 없다면 아래 URL을 임시로 사용할 수 있습니다.
        st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", width=250)

st.write("---")

# --- 자기소개 (About Me) ---
with st.container():
    st.header("About Me")
    st.write(
        """
        - **이름**: 신송배
        - **직업**: 백엔드 개발자 (5년차)
        - **관심사**:
            - 대규모 시스템 아키텍처 설계
        - **목표**: 기술을 통해 사용자에게 실질적인 가치를 제공하는 개발자가 되는 것
        """
    )

st.write("---")

# --- 기술 스택 (Skills) ---
with st.container():
    st.header("My Skills")
    st.write("제가 주로 사용하는 기술들입니다.")

    # 3개의 컬럼으로 나누어 기술을 표시합니다.
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Languages")
        st.write("- `Python`")
        st.write("- `R`")
    with col2:
        st.subheader("Frameworks")
        st.write("- `GCP` / `MySQL`")
    with col3:
        st.subheader("Databases & Tools")
        st.write("- `MySQL` / `Bigquery`")

st.write("---")

# --- 프로젝트 (Projects) --- 
with st.container():
    st.header("Projects pages")
    # # 프로젝트 1
    # image_column, text_column = st.columns((1, 2))
    # with image_column:
    #     # 프로젝트 관련 이미지를 추가합니다.
    #     st.image("https://raw.githubusercontent.com/github/explore/80688e429a7d406f3536e050b34a37731a2ea01f/topics/django/django.png", width=200)
    # with text_column:
    #     st.subheader("실시간 맛집 추천 시스템")
    #     st.write(
    #         """
    #         사용자의 위치와 취향을 기반으로 주변 맛집을 실시간으로 추천하는 API 서버를 개발했습니다.
    #         - **주요 기능**: 맛집 검색, 평점 및 리뷰, 개인화 추천
    #         - **사용 기술**: `Django REST framework`, `Celery`, `Redis`
    #         - **성과**: 추천 정확도 20% 향상 및 API 응답 시간 300ms 이하 달성
    #         """
    #     )
    #     st.markdown("프로젝트 소스코드 보기...")

    st.write("---")


