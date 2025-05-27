import streamlit as st
import yfinance as yf
import plotly.graph_objs as go
from datetime import date

# ---------------------
# 기본 설정
# ---------------------
st.set_page_config(page_title="시가총액 상위 10대 기업 주가 시각화", layout="wide")

st.title("📈 글로벌 시가총액 Top 10 기업 주가 시각화")
st.markdown("""
2024년 기준 글로벌 시가총액 상위 10개 기업 중에서 야후 파이낸스에서 데이터를 제공하는 주요 기업의 주가 추이를 시각화합니다.
""")

# ---------------------
# 티커 및 설정
# ---------------------
company_names = {
    'AAPL': 'Apple',
    'MSFT': 'Microsoft',
    'GOOGL': 'Alphabet (Google)',
    'AMZN': 'Amazon',
    'NVDA': 'NVIDIA',
    'BRK-B': 'Berkshire Hathaway',
    'META': 'Meta Platforms',
    'TSM': 'Taiwan Semiconductor',
    'TSLA': 'Tesla'
}

tickers = list(company_names.keys())

# 날짜 선택
col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("시작 날짜", value=date(2024, 1, 1))
with col2:
    end_date = st.date_input("종료 날짜", value=date(2025, 1, 1))

# 기업 선택
selected_tickers = st.multiselect(
    "시각화할 기업 선택", options=tickers, default=tickers,
    format_func=lambda x: company_names[x]
)

# ---------------------
# 데이터 다운로드
# ---------------------
@st.cache_data
def load_data(tickers, start, end):
    return yf.download(tickers, start=start, end=end, group_by='ticker', auto_adjust=True)

if selected_tickers:
    with st.spinner("📡 데이터를 불러오는 중입니다..."):
        data = load_data(selected_tickers, start_date, end_date)

    # ---------------------
    # Plotly 그래프
    # ---------------------
    fig = go.Figure()
    for ticker in selected_tickers:
        try:
            fig.add_trace(go.Scatter(
                x=data[ticker].index,
                y=data[ticker]['Close'],
                mode='lines',
                name=company_names[ticker]
            ))
        except KeyError:
            st.warning(f"⚠️ {company_names[ticker]}의 데이터를 불러오지 못했습니다.")

    fig.update_layout(
        title="📊 선택한 기업들의 주가 추이",
        xaxis_title="날짜",
        yaxis_title="주가 (USD)",
        legend_title="기업명",
        template="plotly_dark",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("좌측에서 하나 이상의 기업을 선택해주세요.")

