from extract import extract_data
from validation import validate_data
from transform import clean_data
from load import load_data
from visual_checks import save_plots

RAW_PATH = "data/raw_data.csv"
CLEAN_PATH = "data/cleaned_data.csv"

def main():
    print("1) Extracting data...")
    df_raw = extract_data(RAW_PATH)
    print(f"   Loaded rows: {len(df_raw)}")

    print("2) Validating data...")
    results = validate_data(df_raw)
    for k, v in results.items():
        print(f"   {k}: {v}")

    # Stop pipeline if FAIL
    if not str(results.get("status", "")).startswith("PASS"):
        raise SystemExit(f"❌ Pipeline stopped: {results['status']}")

    print("3) Transforming (cleaning) data...")
    df_clean = clean_data(df_raw)
    print(f"   Clean rows: {len(df_clean)}")

    print("4) Loading cleaned data...")
    load_data(df_clean, CLEAN_PATH)
    print(f"   Saved: {CLEAN_PATH}")

    print("5) Visual checks (saving plots)...")
    save_plots(df_clean)
    print("   Saved plots to outputs/plots/")

    print("✅ ETL completed successfully!")

if __name__ == "__main__":
    main()
