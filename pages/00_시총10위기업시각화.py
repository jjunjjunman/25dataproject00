import yfinance as yf
import plotly.graph_objs as go

# 시총 상위 9개 기업 (Yahoo 티커 기준)
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'BRK-B', 'META', 'TSM', 'TSLA']

# 데이터 수집
data = yf.download(tickers, start="2024-01-01", end="2025-01-01")['Adj Close']

# Plotly 시각화
fig = go.Figure()

for ticker in tickers:
    fig.add_trace(go.Scatter(x=data.index, y=data[ticker], mode='lines', name=ticker))

fig.update_layout(
    title='2024년 글로벌 시총 상위 기업 주가 추이',
    xaxis_title='날짜',
    yaxis_title='조정 종가 (USD)',
    legend_title='티커',
    template='plotly_dark'
)

fig.show()
