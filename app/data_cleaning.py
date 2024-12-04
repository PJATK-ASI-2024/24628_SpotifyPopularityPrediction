import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def clean_data(df: pd.DataFrame, feature_names: list):
    """Clean data by handling missing values, duplicates, and scaling features."""
    df = df.drop(columns=["id", "name"], errors="ignore")
    df["explicit"] = df["explicit"].astype(int)

    df = pd.get_dummies(df, columns=["genre"], drop_first=True)

    expected_genres = [col for col in feature_names if col.startswith("genre_")]
    for genre in expected_genres:
        if genre not in df.columns:
            df[genre] = 0

    df["artists_count"] = df["artists"].apply(lambda x: len(x.split(", ")))
    df = df.drop(columns=["artists"], errors="ignore")

    df["album"] = df["album"].astype("category").cat.codes
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)

    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    scaler = StandardScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

    min_max_scaler = MinMaxScaler()
    df[numeric_cols] = min_max_scaler.fit_transform(df[numeric_cols])

    for col in feature_names:
        if col not in df.columns:
            df[col] = 0

    df = df[feature_names]
    return df