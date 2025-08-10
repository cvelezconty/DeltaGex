# gexbot-charts

Pulls live metrics from GEXBot (Delta GEX, Charm, Convexity) and renders linear charts.

## Quick Start (Windows)
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt

python src\fetch_once.py     # one-time pull & chart
python src\run_live.py       # live loop (Ctrl+C to stop)
