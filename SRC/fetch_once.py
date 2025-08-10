import os, time, json
from src.util import load_cfg, append_json
from src.gex_client import GEXClient
from src.plotter import plot_metrics

def main():
    cfg = load_cfg()
    client = GEXClient(cfg["api"]["gexbot_url"], cfg["api"]["gexbot_key"], cfg["instrument"]["ticker"])

    os.makedirs(cfg["io"]["data_dir"], exist_ok=True)
    os.makedirs(cfg["io"]["charts_dir"], exist_ok=True)
    metrics_file = os.path.join(cfg["io"]["data_dir"], cfg["io"]["metrics_file"])

    data = client.fetch_latest(span="5min")
    sample = {
        "time": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "asof": float(data.get("asof", time.time())),
        "spot": float(data.get("spot", 0.0)),
        "net_gex": float(data.get("net_gex", 0.0)),
        "net_charm": float(data.get("net_charm", 0.0)),
        "net_convexity": float(data.get("net_convexity", 0.0))
    }
    append_json(metrics_file, sample)

    hist = json.load(open(metrics_file,"r",encoding="utf-8"))
    plot_metrics(os.path.join(cfg["io"]["charts_dir"],"live_trends.png"), hist)
    print("Fetch OK. Wrote JSON and chart.")

if __name__ == "__main__":
    main()
