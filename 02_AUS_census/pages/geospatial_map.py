import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Geospatial Map", layout="wide")
st.title("📍 Sydney Interactive Maps")

# 지도 선택 로직
map_choice = st.selectbox("지도를 선택하세요", ["SEIFA- IRSAD and IRSD Map","IRSAD and IRSD Gap Map"])
file_map = {
    "SEIFA- IRSAD and IRSD Map": "../01_SEIFA_analyse/sydney_comparison_map.html",
    "IRSAD and IRSD Gap Map": "../01_SEIFA_analyse/sydney_gap_map.html",
}

with open(file_map[map_choice], 'r', encoding='utf-8') as f:
    html_data = f.read()
components.html(html_data, height=700)