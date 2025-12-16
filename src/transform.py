import pandas as pd

def clean_data(df):
    df = df.dropna()             # remove rows with missing values
    df = df.drop_duplicates()    # remove duplicate rows
    df = df[df["orders"] >= 0]   # remove negative orders
    df["date"] = pd.to_datetime(df["date"])  # convert date text → real date
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/raw_data.csv")
    clean_df = clean_data(df)
    print(clean_df)
