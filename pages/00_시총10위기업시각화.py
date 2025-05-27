import yfinance as yf
import plotly.graph_objs as go

# 시총 상위 9개 기업 (야후 파이낸스 티커)
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'NVDA', 'BRK-B', 'META', 'TSM', 'TSLA']

# 데이터 수집 (다중 종목 시 MultiIndex columns 생성됨)
data = yf.download(tickers, start="2024-01-01", end="2025-01-01", group_by='ticker')

# Plotly 시각화
import plotly.graph_objs as go

fig = go.Figure()

for ticker in tickers:
    try:
        fig.add_trace(go.Scatter(
            x=data[ticker].index,
            y=data[ticker]['Adj Close'],
            mode='lines',
            name=ticker
        ))
    except KeyError:
        print(f"데이터 누락: {ticker}")

fig.update_layout(
    title='2024년 글로벌 시총 상위 기업 주가 추이',
    xaxis_title='날짜',
    yaxis_title='조정 종가 (USD)',
    legend_title='티커',
    template='plotly_dark'
)

fig.show()
