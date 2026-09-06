import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Sunny Dhan-Quant Pro",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Dark Mobile-Optimized Quant Styling
st.markdown("""
<style>
    .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0rem;
        padding-left: 0.2rem;
        padding-right: 0.2rem;
    }
    .main { background-color: #0b0e14; }
    header { visibility: hidden; }
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# Complete Dhan + TradingView Native Hybrid Widget
dhan_hybrid_html = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
    <script src="https://unpkg.com/lightweight-charts@4.2.1/dist/lightweight-charts.standalone.production.js"></script>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background: #0c1017; color: #fff; overflow-x: hidden; }
        
        /* Dhan Top Header */
        .dhan-top-bar {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 8px 12px;
            background: #111622;
            border-bottom: 1px solid #1e2638;
        }
        .symbol-badge {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .dhan-logo {
            background: #00b074;
            color: white;
            font-weight: 800;
            border-radius: 50%;
            width: 28px;
            height: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 15px;
        }
        .price-text {
            font-size: 17px;
            font-weight: 700;
            color: #ffffff;
        }
        .change-text {
            font-size: 12px;
            color: #00f59b;
            font-weight: 600;
        }
        
        /* Timeframe Navigation Bar */
        .tf-bar {
            display: flex;
            align-items: center;
            background: #0d121c;
            padding: 4px 10px;
            gap: 6px;
            border-bottom: 1px solid #1a2233;
            overflow-x: auto;
        }
        .tf-btn {
            background: transparent;
            border: none;
            color: #7d8b9e;
            padding: 4px 8px;
            font-size: 12px;
            font-weight: 600;
            border-radius: 4px;
            cursor: pointer;
        }
        .tf-btn.active {
            background: #1f293d;
            color: #00f59b;
        }

        /* Chart Canvas Area */
        #chart-container {
            position: relative;
            width: 100%;
            height: 480px;
        }

        /* Dhan Floating Buy/Sell Interactive Cards */
        .floating-order-box {
            position: absolute;
            top: 15px;
            left: 12px;
            z-index: 10;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }
        .order-pill {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 110px;
            padding: 5px 8px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0,0,0,0.4);
            border: 1px solid rgba(255,255,255,0.1);
        }
        .sell-pill {
            background: rgba(239, 68, 68, 0.15);
            color: #ff4b5c;
            border-left: 3px solid #ff4b5c;
        }
        .buy-pill {
            background: rgba(59, 130, 246, 0.15);
            color: #3b82f6;
            border-left: 3px solid #3b82f6;
        }

        /* Dhan Bottom Dock */
        .bottom-dock {
            display: flex;
            justify-content: space-around;
            padding: 8px 10px;
            background: #111622;
            border-top: 1px solid #1e2638;
            margin-top: 4px;
        }
        .dock-tab {
            display: flex;
            align-items: center;
            gap: 6px;
            background: #182030;
            padding: 8px 14px;
            border-radius: 8px;
            font-size: 12px;
            font-weight: 600;
            color: #e2e8f0;
            border: 1px solid #233047;
            cursor: pointer;
        }
        .dock-tab.primary {
            background: linear-gradient(135deg, #1e3a8a, #2563eb);
            border-color: #3b82f6;
            color: #fff;
        }
    </style>
</head>
<body>

    <!-- Dhan Header -->
    <div class="dhan-top-bar">
        <div class="symbol-badge">
            <div class="dhan-logo">ध</div>
            <div>
                <div style="font-size: 13px; font-weight: 700;">NIFTY 50</div>
                <div class="change-text">+24.25 (+0.10%) 🟢</div>
            </div>
        </div>
        <div class="price-text" id="live-price">23,897.70</div>
    </div>

    <!-- Timeframes Bar -->
    <div class="tf-bar">
        <button class="tf-btn">1m</button>
        <button class="tf-btn">5m</button>
        <button class="tf-btn active">15m</button>
        <button class="tf-btn">1h</button>
        <button class="tf-btn">D</button>
        <span style="color: #303e55; margin: 0 4px;">|</span>
        <span style="font-size: 11px; color: #00f59b; font-weight: 600;">⚡ Supertrend Active</span>
    </div>

    <!-- Chart Screen with Floating Buy/Sell -->
    <div id="chart-container">
        <div class="floating-order-box">
            <div class="order-pill sell-pill">
                <span>SELL</span>
                <span id="sell-price">23,897.70</span>
            </div>
            <div class="order-pill buy-pill">
                <span>BUY</span>
                <span id="buy-price">23,897.70</span>
            </div>
        </div>
    </div>

    <!-- Dhan Bottom Navigation Dock -->
    <div class="bottom-dock">
        <div class="dock-tab">
            <span>📑</span> Chain
        </div>
        <div class="dock-tab primary">
            <span>⚡</span> Scalper Pro
        </div>
        <div class="dock-tab">
            <span>⚡</span> Flash Trade
        </div>
    </div>

    <script>
        const chartContainer = document.getElementById('chart-container');
        const chart = LightweightCharts.createChart(chartContainer, {
            width: chartContainer.clientWidth,
            height: 480,
            layout: {
                background: { color: '#0c1017' },
                textColor: '#7d8b9e',
            },
            grid: {
                vertLines: { color: 'rgba(30, 38, 56, 0.4)' },
                horzLines: { color: 'rgba(30, 38, 56, 0.4)' },
            },
            crosshair: {
                mode: LightweightCharts.CrosshairMode.Normal,
            },
            rightPriceScale: {
                borderColor: '#1e2638',
                visible: true,
            },
            timeScale: {
                borderColor: '#1e2638',
                timeVisible: true,
                secondsVisible: false,
            },
        });

        // Candlestick Series
        const candleSeries = chart.addCandlestickSeries({
            upColor: '#00f59b',
            downColor: '#ff3b69',
            borderUpColor: '#00f59b',
            borderDownColor: '#ff3b69',
            wickUpColor: '#00f59b',
            wickDownColor: '#ff3b69',
        });

        // Generate Nifty Realistic Wave Data
        let baseTime = Math.floor(Date.now() / 1000) - (60 * 15 * 60);
        let baseVal = 23820;
        let candleData = [];
        let supertrendData = [];

        for (let i = 0; i < 60; i++) {
            let open = baseVal + (Math.random() - 0.48) * 18;
            let high = open + Math.random() * 22;
            let low = open - Math.random() * 20;
            let close = (open + high + low) / 3;
            baseVal = close;

            let time = baseTime + (i * 900);
            candleData.push({ time, open, high, low, close });

            // Supertrend baseline
            supertrendData.push({
                time,
                value: close > open ? low - 10 : high + 10
            });
        }

        candleSeries.setData(candleData);

        // Supertrend Line (Green/Red Band)
        const supertrendLine = chart.addLineSeries({
            color: '#00e676',
            lineWidth: 2,
            lineStyle: LightweightCharts.LineStyle.Solid,
        });
        supertrendLine.setData(supertrendData);

        // Buy/Sell Markers on Chart
        candleSeries.setMarkers([
            {
                time: candleData[candleData.length - 15].time,
                position: 'belowBar',
                color: '#2196F3',
                shape: 'arrowUp',
                text: 'BUY @ 23,840'
            },
            {
                time: candleData[candleData.length - 2].time,
                position: 'aboveBar',
                color: '#F44336',
                shape: 'arrowDown',
                text: 'BREAKOUT'
            }
        ]);

        // Auto Resize on Screen Rotation / Viewport Changes
        window.addEventListener('resize', () => {
            chart.applyOptions({ width: chartContainer.clientWidth });
        });

        // Live Ticking Engine
        setInterval(() => {
            const lastCandle = candleData[candleData.length - 1];
            const tickChange = (Math.random() - 0.49) * 2.5;
            const newClose = +(lastCandle.close + tickChange).toFixed(2);
            lastCandle.close = newClose;
            if (newClose > lastCandle.high) lastCandle.high = newClose;
            if (newClose < lastCandle.low) lastCandle.low = newClose;

            candleSeries.update(lastCandle);
            document.getElementById('live-price').innerText = newClose.toFixed(2);
            document.getElementById('sell-price').innerText = newClose.toFixed(2);
            document.getElementById('buy-price').innerText = newClose.toFixed(2);
        }, 1200);
    </script>
</body>
</html>
"""

components.html(dhan_hybrid_html, height=590)

# Bottom Quant Auto-Execution Trigger
st.markdown("### ⚡ AI Execution Controller")
col_b1, col_b2 = st.columns(2)
col_b1.button("🟢 Start Auto-Scalper", use_container_width=True)
col_b2.button("🔴 Emergency Kill Switch", use_container_width=True)
