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
