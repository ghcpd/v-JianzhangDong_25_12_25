import csv
import statistics
import yaml
from pathlib import Path


def load_csv(path: str) -> list:
    """Load CSV using csv module."""
    file = Path(path)
    if not file.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")
    with open(path, 'r') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    if not data:
        raise ValueError("CSV cannot be empty")
    return data


def load_config(path: str) -> dict:
    """Load YAML config file."""
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def normalize_column(data: list, col: str) -> list:
    """Normalize data using statistics."""
    if not data or col not in data[0]:
        raise KeyError(f"Column {col} not found in data.")
    values = [float(row[col]) for row in data if row[col]]
    mean = statistics.mean(values)
    stdev = statistics.stdev(values)
    return [(x - mean) / stdev for x in values]
