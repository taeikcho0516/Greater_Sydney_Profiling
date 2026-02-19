import streamlit as st

# 1. 페이지 설정 (모든 페이지의 기본 설정이 됩니다)
st.set_page_config(
    page_title="Sydney Socio-Economic Dashboard",
    page_icon="🇦🇺",
    layout="wide"
)

# 2. 메인 제목 및 소개
st.title("🇦🇺 Sydney Socio-Economic Disparity Analysis")
st.markdown("### 시드니 광역권 사회경제적 격차 분석 프로젝트")

st.divider()

# 3. 프로젝트 핵심 요약 (README 기반)
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📌 Project Overview")
    st.write("""
    본 프로젝트는 호주 통계청(ABS)의 데이터를 활용하여 시드니 내의 사회경제적 불평등을 분석합니다. 
    단순한 지표 비교를 넘어, 'Latte Line'으로 대표되는 지리적 분단과 
    젠트리피케이션이 진행 중인 지역들을 데이터로 증명합니다.
    """)

with col2:
    st.subheader("🎯 Key Objectives")
    st.write("- **Data Integration**: SEIFA 2021 데이터와 디지털 경계 파일 결합")
    st.write("- **Geospatial Analysis**: 인터랙티브 지도를 통한 'Latte Line' 시각화")
    st.write("- **Gap Analysis**: IRSD와 IRSAD의 격차를 통한 숨겨진 부유층/소외층 식별")

st.divider()

# 4. 내비게이션 안내
st.info("👈 왼쪽 사이드바의 메뉴를 통해 주제별 상세 분석을 확인하실 수 있습니다.")

# 5. 주요 인사이트 미리보기 (이미지 활용)
st.subheader("💡 주요 분석 대상 지역")
cols = st.columns(3)
with cols[0]:
    st.metric(label="Haymarket", value="Gap +7", delta="Student & Luxury Mix")
with cols[1]:
    st.metric(label="Waterloo", value="Gap +6", delta="Gentrification Case")
with cols[2]:
    st.metric(label="Burwood", value="Gap +4", delta="Strong Economic Resources")