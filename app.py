import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Sunny AI Quant Terminal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Dark Theme CSS
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #161b22; border-radius: 8px; padding: 10px; border: 1px solid #30363d; }
</style>
""", unsafe_allow_html=True)

st.title("⚡ AI Autonomous Quant Terminal")
st.caption("Live Strategy Engine • Powered by DhanHQ & AI Sentiment")

# Top Metrics Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("NIFTY 50", "24,850.20", "+124.50 (+0.50%)")
col2.metric("BANK NIFTY", "51,200.80", "-85.30 (-0.17%)")
col3.metric("AI Market Bias", "BULLISH (78%)", "Strong Buy")
col4.metric("Live P&L", "+₹14,250", "3 Active Positions")

st.divider()

# Main Dashboard Layout
left_col, right_col = st.columns([2, 1])

with left_col:
    st.subheader("📈 Multi-Timeframe Trend & Projection")
    chart_data = pd.DataFrame(
        np.random.randn(25, 3) + [24800, 24820, 24850],
        columns=["1m Price", "5m Trend", "15m Projection"]
    )
    st.line_chart(chart_data)

with right_col:
    st.subheader("🤖 AI Sentiment & Signals")
    st.success("🟢 NIFTY: Bullish Flag Breakout detected on 5M timeframe.")
    st.info("ℹ️ Global Macro: Asian markets positive, crude oil stabilizing.")
    st.warning("⚠️ Risk Protocol: Max Drawdown locked at 2% daily limit.")

st.divider()

# Control Panel
st.subheader("⚙️ System Status")
st.write("Broker Connectivity: **DhanHQ Ready** | Auto-Execution: **Monitoring Active**")

