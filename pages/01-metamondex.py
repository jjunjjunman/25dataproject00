import streamlit as st
import requests

# Streamlit 페이지 설정
st.set_page_config(page_title="포켓몬 정보 도감", page_icon="⚡")
st.title("🧿 포켓몬 정보 도감")

# 사용자 입력
pokemon_name = st.text_input("포켓몬 이름을 입력하세요 (예: pikachu, bulbasaur 등)").lower().strip()

# PokeAPI에서 데이터 가져오기
def get_pokemon_data(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    return None

# 정보 출력
if pokemon_name:
    data = get_pokemon_data(pokemon_name)

    if data:
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(data["sprites"]["front_default"], caption=f"{pokemon_name.title()}")

        with col2:
            st.subheader(f"📌 이름: {data['name'].title()}")
            types = ", ".join([t["type"]["name"].title() for t in data["types"]])
            st.markdown(f"**🌈 타입:** {types}")
            st.markdown(f"**📏 키:** {data['height'] / 10} m")
            st.markdown(f"**⚖️ 몸무게:** {data['weight'] / 10} kg")
            st.markdown("**📊 스탯:**")
            for stat in data["stats"]:
                st.markdown(f"- {stat['stat']['name'].title()}: {stat['base_stat']}")
    else:
        st.error("❌ 해당 포켓몬을 찾을 수 없습니다. 이름을 다시 확인해주세요.")
else:
    st.info("포켓몬 이름을 입력해 정보를 확인해보세요!")
