from pathlib import Path
from urllib.request import urlopen


# Public Sample Superstore CSV
DATA_URL = (
    "https://raw.githubusercontent.com/sumit0072/Superstore-Data-Analysis/main/Sample%20-%20Superstore.csv"
)

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Raw data directory and file
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"
RAW_DATA_FILE = RAW_DATA_DIR / "sales_data.csv"


def download_sales_data():
    """Download the raw sales dataset and save it locally."""

    # Create the directory if it does not exist
    RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

    print("Downloading sales dataset...")

    try:
        with urlopen(DATA_URL) as response:
            data = response.read()

        RAW_DATA_FILE.write_bytes(data)

        print("Download completed successfully.")
        print(f"Saved to: {RAW_DATA_FILE}")
        print(f"File size: {RAW_DATA_FILE.stat().st_size:,} bytes")

    except Exception as error:
        print("Download failed.")
        print(f"Error: {error}")


if __name__ == "__main__":
    download_sales_data()