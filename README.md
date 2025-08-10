
# gexbot-charts

Pulls live metrics from GEXBot (Delta GEX, Vanna, Charm) and renders rolling linear charts.

## Features
- Fetch `net_gex`, `net_vanna`, `net_charm` from the GEXBot Orderflow API
- Store rolling metrics as JSON
- Plot linear time series (Matplotlib; no seaborn)
- Run once (`fetch_once.py`) or in a loop (`run_live.py`)

## Quick Start

### 1) Clone and configure
```bash
git clone https://github.com/your-org/gexbot-charts.git
cd gexbot-charts
# Windows
copy config.example.json config.json
# macOS/Linux
cp config.example.json config.json
```
Edit `config.json` with your API key and preferences.

### 2) Install
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### 3) Fetch once (sanity check)
```bash
python src/fetch_once.py
```
Expected output:
- `data/metrics.json` (append-only, latest samples kept)
- `charts/live_trends.png` (linear chart of Delta GEX, Vanna, Charm)

### 4) Run in a loop (live mode)
```bash
python src/run_live.py
```
Press `Ctrl+C` to stop.

## Config
`config.json`:
```json
{
  "api": {
    "gexbot_url": "https://www.gexbot.com/orderflow",
    "gexbot_key": "YOUR_API_KEY"
  },
  "instrument": { "ticker": "SPX->ES" },
  "poll": { "interval_sec": 5 },
  "io": {
    "charts_dir": "charts",
    "data_dir": "data",
    "metrics_file": "metrics.json"
  }
}
```

## Notes
- This repository **does not** interact with trading platforms.
- Charts are plain Matplotlib line plots for simplicity and portability.
- If your API requires different authentication, adjust `gex_client.py` accordingly.

## License
MIT
