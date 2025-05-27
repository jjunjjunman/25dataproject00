import streamlit as st
import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# 예시용 고등학교 데이터 (실제 데이터로 교체 가능)
school_data = [
    {"name": "서울고등학교", "address": "서울 서초구 반포대로 100", "lat": 37.5002, "lon": 127.0115},
    {"name": "세화고등학교", "address": "서울 서초구 반포대로 120", "lat": 37.5025, "lon": 127.0127},
    {"name": "반포고등학교", "address": "서울 서초구 고무래로 1", "lat": 37.4978, "lon": 127.0071},
    {"name": "상문고등학교", "address": "서울 서초구 남부순환로 230", "lat": 37.4861, "lon": 127.0110}
]

df = pd.DataFrame(school_data)

# Streamlit 앱 제목
st.title("서초구 고등학교 지도")

# Folium 지도 생성
m = folium.Map(location=[37.4919, 127.0134], zoom_start=13)

# 마커 추가
for _, row in df.iterrows():
    folium.Marker(
        location=[row["lat"], row["lon"]],
        popup=f"{row['name']}<br>{row['address']}",
        tooltip=row["name"],
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(m)

# 지도 렌더링
st_folium(m, width=700, height=500)

# 선택 필터 (옵션)
selected_school = st.selectbox("학교 선택", df["name"])
school_info = df[df["name"] == selected_school].iloc[0]
st.write(f"**주소**: {school_info['address']}")
