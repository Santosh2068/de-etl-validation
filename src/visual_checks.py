import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

PLOTS_DIR = Path("outputs/plots")

def save_plots(df: pd.DataFrame):
    PLOTS_DIR.mkdir(parents=True, exist_ok=True)

    # Histogram
    plt.figure()
    df["orders"].plot(kind="hist", bins=10, title="Orders distribution")
    plt.savefig(PLOTS_DIR / "orders_hist.png", dpi=150, bbox_inches="tight")
    plt.close()

    # Box plot
    plt.figure()
    df["revenue"].plot(kind="box", title="Revenue outliers")
    plt.savefig(PLOTS_DIR / "revenue_box.png", dpi=150, bbox_inches="tight")
    plt.close()

    # Time series
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    daily = df.groupby(df["date"].dt.date)["orders"].sum()

    plt.figure()
    daily.plot(kind="line", title="Daily Orders Trend")
    plt.savefig(PLOTS_DIR / "daily_orders_trend.png", dpi=150, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    df = pd.read_csv("data/raw_data.csv")
    save_plots(df)
    print("Saved plots to outputs/plots/")
