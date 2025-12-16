import pandas as pd

def validate_data(df: pd.DataFrame) -> dict:
    checks = {}

    # Basic checks
    checks["row_count"] = len(df)
    checks["duplicate_rows"] = int(df.duplicated().sum())

    # Null checks
    null_counts = df.isnull().sum()
    checks["null_counts"] = null_counts.to_dict()

    # Business rules
    checks["negative_orders"] = int((df["orders"] < 0).sum())
    checks["negative_revenue"] = int((df["revenue"] < 0).sum())

    # PASS/FAIL rules (tweakable)
    checks["status"] = "PASS"

    if checks["row_count"] == 0:
        checks["status"] = "FAIL (no rows)"

    if checks["duplicate_rows"] > 0:
        checks["status"] = "FAIL (duplicates found)"

    if checks["negative_orders"] > 0 or checks["negative_revenue"] > 0:
        checks["status"] = "FAIL (negative values found)"

    if null_counts.sum() > 0:
        checks["status"] = "FAIL (null values found)"

    return checks


if __name__ == "__main__":
    df = pd.read_csv("data/raw_data.csv")
    results = validate_data(df)

    for k, v in results.items():
        print(f"{k}: {v}")
