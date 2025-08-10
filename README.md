# gexbot-charts

Pulls live metrics from GEXBot (Delta GEX, Charm, Convexity) and renders normalized line charts for intraday monitoring.

## Features
- Live polling of GEXBot API
- Tracks **Delta GEX**, **Charm**, **Convexity**
- Saves rolling JSON history
- Generates Matplotlib charts in `charts/live_trends.png`

## Setup
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
