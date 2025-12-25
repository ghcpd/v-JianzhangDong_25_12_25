from app.data_loader import load_csv, normalize_column
import csv

# Create a temp CSV (no external files needed)
with open("tmp.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["value"])
    for v in [1, 2, 3, 4, 5]:
        writer.writerow([v])

data = load_csv("tmp.csv")
norm = normalize_column(data, "value")

print("Normalization OK:", norm[:3])
