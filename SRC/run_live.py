import os, time, json, signal
from src.util import load_cfg, append_json
from src.gex_client import GEXClient
from src.plotter import plot_metrics

RUN = True
def handle_sig(sig, frame):
    global RUN
    RUN = False

def main():
    signal.signal(signal.SIGINT, handle_sig)
    signal.signal(signal.SIGTERM, handle_sig)

    cfg = load_cfg()
    client = GEXClient(cfg["api"]["gexbot_url"], cfg["api"]["gexbot_key"], cfg["instrument"]["ticker"])

    os.makedirs(cfg["io"]["data_dir"], exist_ok=True)
    os.makedirs(cfg["io"]["charts_dir"], exist_ok=True)
    metrics_file = os.path.join(cfg["io"]["data_dir"], cfg["io"]["metrics_file"])

    interval = int(cfg["poll"]["interval_sec"])
    print("Starting live loop... Ctrl+C to stop.")
    while RUN:
        try:
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

            print(f"{sample['time']} | spot {sample['spot']:.2f} | ΔGEX {sample['net_gex']:.0f} | Charm {sample['net_charm']:.0f} | Convexity {sample['net_convexity']:.0f}")
        except Exception as e:
            print("Error:", e)

        time.sleep(max(1, interval))

if __name__ == "__main__":
    main()
