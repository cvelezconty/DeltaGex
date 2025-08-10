import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def _norm(series):
    if not series: return series
    denom = max(1e-9, max(abs(x) for x in series))
    return [x / denom for x in series]

def plot_metrics(outfile, hist):
    if not hist: return

    t   = [h["asof"] for h in hist]
    dg  = [h["net_gex"] for h in hist]
    ch  = [h["net_charm"] for h in hist]
    cx  = [h["net_convexity"] for h in hist]

    dgN, chN, cxN = _norm(dg), _norm(ch), _norm(cx)

    plt.figure(figsize=(10,4))
    plt.plot(t, dgN, label="ΔGEX (norm)")
    plt.plot(t, chN, label="Charm (norm)")
    plt.plot(t, cxN, label="Convexity (norm)")
    plt.legend(loc="upper left")
    plt.title("GEXBot Live Trends (normalized)")
    plt.xlabel("epoch")
    plt.ylabel("normalized")
    plt.tight_layout()
    plt.savefig(outfile, dpi=120)
    plt.close()
