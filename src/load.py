import pandas as pd
from transform import clean_data

def load_data(df, path):
    df.to_csv(path, index=False)

if __name__ == "__main__":
    df = pd.read_csv("data/raw_data.csv")
    df_clean = clean_data(df)
    load_data(df_clean, "data/cleaned_data.csv")
    print("Saved cleaned data to data/cleaned_data.csv")
