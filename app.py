import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta

st.set_page_config(
    page_title="Sunny AI Quant Terminal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark Quant Theme CSS
st.markdown("""
<style>
    .main { background-color: #0b0e14; }
    .stMetric { background-color: #121824; border-radius: 8px; padding: 12px; border: 1px solid #1f293d; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { background-color: #121824; border-radius: 6px; padding: 8px 16px; color: #8b949e; }
    .stTabs [aria-selected="true"] { background-color: #238636; color: white; }
</style>
""", unsafe_allow_html=True)

# Top Bar
st.title("⚡ Sunny AI Quant Terminal")
st.caption("Autonomous Execution Engine • Multi-Timeframe Matrix • AI Sentiment")

# Top KPI Matrix
m1, m2, m3, m4 = st.columns(4)
m1.metric("NIFTY 50", "24,862.40", "+136.70 (+0.55%)")
m2.metric("BANK NIFTY", "51,340.15", "+210.60 (+0.41%)")
m3.metric("AI Bias (Multi-TF)", "STRONG BUY", "Score: +84/100")
m4.metric("Virtual P&L (Paper)", "+₹18,450", "Win Rate: 76%")

st.divider()

# Layout: Chart on Left (70%), AI Intel on Right (30%)
chart_col, intel_col = st.columns([7, 3])

with chart_col:
    st.subheader("📊 Live Multi-Timeframe Price Projection")
    
    # Timeframe Selector Tabs
    tab_1m, tab_5m, tab_15m = st.tabs(["⚡ 1-Minute (Scalping)", "⏱️ 5-Minute (Trend)", "🕒 15-Minute (Macro)"])
    
    def generate_candles(n_bars, base_price, volatility):
        dates = [datetime.now() - timedelta(minutes=(n_bars - i) * 5) for i in range(n_bars)]
        opens = [base_price]
        for _ in range(1, n_bars):
            opens.append(opens[-1] + np.random.normal(0, volatility))
        
        opens = np.array(opens)
        highs = opens + np.abs(np.random.normal(0, volatility * 1.2, n_bars))
        lows = opens - np.abs(np.random.normal(0, volatility * 1.2, n_bars))
        closes = opens + np.random.normal(0, volatility, n_bars)
        
        return pd.DataFrame({'Date': dates, 'Open': opens, 'High': highs, 'Low': lows, 'Close': closes})

    def render_candlestick(df, title):
        fig = go.Figure(data=[go.Candlestick(
            x=df['Date'],
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            increasing_line_color='#00F59B',
            decreasing_line_color='#FF3B69',
            name="Price"
        )])
        
        # Add EMA 20 Dynamic Trendline
        ema20 = df['Close'].ewm(span=10).mean()
        fig.add_trace(go.Scatter(x=df['Date'], y=ema20, line=dict(color='#00D4FF', width=1.5), name="EMA Trend"))
        
        fig.update_layout(
            template="plotly_dark",
            height=420,
            margin=dict(l=10, r=10, t=10, b=10),
            paper_bgcolor="#0b0e14",
            plot_bgcolor="#0b0e14",
            xaxis_rangeslider_visible=False,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        return fig

    with tab_1m:
        st.plotly_chart(render_candlestick(generate_candles(40, 24840, 4), "1M"), use_container_width=True)
    with tab_5m:
        st.plotly_chart(render_candlestick(generate_candles(40, 24800, 10), "5M"), use_container_width=True)
    with tab_15m:
        st.plotly_chart(render_candlestick(generate_candles(40, 24700, 22), "15M"), use_container_width=True)

with intel_col:
    st.subheader("🤖 AI Sentiment Engine")
    
    st.markdown("""
    **Global Macro Matrix:**
    * **US Dow Futures:** `+0.42% 🟢 Bullish`
    * **Brent Crude:** `$78.10 ⚪ Stable`
    * **FII Cash Flow:** `+₹1,840 Cr (Net Buy)`
    """)
    
    st.success("🎯 **Signal:** 5M Pullback Confirmation -> Target: 24,920 | SL: 24,810")
    st.info("🧠 **Sentiment Insight:** High volume buying detected near support zone.")
    st.warning("🛡️ **Safety Guard:** Circuit breaker active at -₹5,000 daily loss.")

st.divider()

# Bottom Control Center
c1, c2, c3 = st.columns(3)
c1.button("🟢 Start Autonomous Loop", use_container_width=True)
c2.button("🟡 Pause Execution", use_container_width=True)
c3.button("🔴 Emergency Square Off All", use_container_width=True)


