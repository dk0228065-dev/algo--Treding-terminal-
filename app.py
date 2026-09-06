import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sunny Pro Quant Terminal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom Styling to match Dhan App UI
st.markdown("""
<style>
    /* Remove padding around canvas */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 0rem;
        padding-left: 0.5rem;
        padding-right: 0.5rem;
    }
    .main {
        background-color: #0d1117;
    }
    .stMetric {
        background-color: #161b22;
        border-radius: 8px;
        padding: 6px 12px;
        border: 1px solid #30363d;
    }
</style>
""", unsafe_allow_html=True)

# Top Bar Header
top1, top2, top3 = st.columns([2, 1, 1])
with top1:
    st.markdown("### ⚡ **Sunny Quant Terminal** `(Dhan-TV Engine)`")
with top2:
    symbol = st.selectbox("", ["INDEX:NIFTY", "INDEX:BANKNIFTY", "BSE:SENSEX"], label_visibility="collapsed")
with top3:
    st.success("🟢 Dhan Feed: Connected")

# Top Fast Metrics
k1, k2, k3, k4 = st.columns(4)
k1.metric("NIFTY 50", "24,850.20", "+124.50 (+0.50%)")
k2.metric("BANK NIFTY", "51,200.80", "-85.30 (-0.17%)")
k3.metric("AI Bias", "BULLISH (78%)", "Breakout Zone")
k4.metric("Live P&L", "+₹14,250", "Auto-Trail SL Active")

# Real TradingView Terminal Widget (Same Engine Dhan Uses)
tradingview_code = f"""
<div class="tradingview-widget-container" style="height:620px;width:100%;">
  <div id="tradingview_full_chart" style="height:100%;width:100%;"></div>
  <script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
  <script type="text/javascript">
  new TradingView.widget(
  {{
    "autosize": true,
    "symbol": "{symbol}",
    "interval": "15",
    "timezone": "Asia/Kolkata",
    "theme": "dark",
    "style": "1",
    "locale": "in",
    "toolbar_bg": "#0d1117",
    "enable_publishing": false,
    "allow_symbol_change": true,
    "withdateranges": true,
    "hide_side_toolbar": false,
    "save_image": true,
    "container_id": "tradingview_full_chart",
    "studies": [
      "Supertrend@tv-basicstudies",
      "MASimple@tv-basicstudies"
    ],
    "show_popup_button": true,
    "popup_width": "1000",
    "popup_height": "650"
  }}
  );
  </script>
</div>
"""

components.html(tradingview_code, height=630)

# Bottom Trading & Algo Execution Desk
st.markdown("---")
c1, c2, c3, c4 = st.columns(4)
c1.button("🟢 AUTO BUY (Market)", use_container_width=True)
c2.button("🔴 AUTO SELL (Market)", use_container_width=True)
c3.button("⚙️ Quant Algo Loop: ON", use_container_width=True)
c4.button("🛑 EMERGENCY EXIT", use_container_width=True)
