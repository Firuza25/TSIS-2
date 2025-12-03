# src/cleaner.py
from pathlib import Path

import logging 
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

DATA_DIR = Path(__file__).resolve().parents[1] / "data"
RAW_PATH = DATA_DIR / "raw_tengri.csv"
CLEAN_PATH = DATA_DIR / "clean_tengri.csv"


def clean_tengri():
    logger.info(" Cleaning Tengrinews data")

    if not RAW_PATH.exists():
        raise FileNotFoundError(f"Raw file not found: {RAW_PATH}")

    df = pd.read_csv(RAW_PATH)

    # normalization
    df["title"] = df["title"].astype(str).str.strip()
    df["link"] = df["link"].astype(str).str.strip()
    df["category"] = df["category"].astype(str).str.strip().str.lower()
    df["image"] = df["image"].astype(str).str.strip()

    # Drop rows with missing crucial fields
    df = df[(df["title"] != "") & (df["link"] != "")]

    # Remove duplicates by link
    before = len(df)
    df = df.drop_duplicates(subset=["link"])
    after = len(df)
    print(f"Removed {before - after} duplicate rows")

    # Try to parse date_raw into proper datetime
    if "date_raw" in df.columns:
        df["date_parsed"] = pd.to_datetime(df["date_raw"], errors="coerce")
        # For DB save as ISO string; NaT → None
        df["date_parsed"] = df["date_parsed"].dt.strftime("%Y-%m-%d %H:%M:%S")

    # Add has_image flag (bool)
    df["has_image"] = df["image"].apply(lambda x: str(x).lower() != "n/a")

    # At the end, ensure at least 100 records
    if len(df) < 100:
       logger.warning(f"Only {len(df)} records after cleaning (required ≥ 100)")

    df.to_csv(CLEAN_PATH, index=False)
    logger.info(f"Saved cleaned data to {CLEAN_PATH}, total rows: {len(df)}")

if __name__ == "__main__":
    clean_tengri()
