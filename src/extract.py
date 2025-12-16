import pandas as pd

def extract_data(path):
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = extract_data("data/raw_data.csv")
    print(df.head())
