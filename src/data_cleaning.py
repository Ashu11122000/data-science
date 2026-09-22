from pathlib import Path

import pandas as pd


# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Input and output files
RAW_DATA_FILE = PROJECT_ROOT / "data" / "raw" / "sales_data.csv"
CLEANED_DATA_FILE = (
    PROJECT_ROOT / "data" / "processed" / "cleaned_sales_data.csv"
)


def clean_sales_data():
    """Load, clean, transform, and save the sales dataset."""

    # Load raw data
    df = pd.read_csv(RAW_DATA_FILE, encoding="latin1")

    # Fill missing Profit values with the median Profit
    df["Profit"] = df["Profit"].fillna(df["Profit"].median())

    # Create calculated Profit_Margin column
    df["Profit_Margin"] = df["Profit"] / df["Sales"]

    # Create output directory if needed
    CLEANED_DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Save cleaned dataset
    df.to_csv(CLEANED_DATA_FILE, index=False)

    print("Sales data cleaned successfully.")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"Saved to: {CLEANED_DATA_FILE}")

    return df


if __name__ == "__main__":
    clean_sales_data()