import csv
import os
import sys
from collections import defaultdict
from datetime import datetime

CSV_PATH = sys.argv[1] if len(sys.argv) > 1 else "data/delegations.csv"

if not os.path.exists(CSV_PATH):
    print(f"CSV file not found: {CSV_PATH}")
    print("Usage: python3 src/tracker.py [csv_path]")
    sys.exit(1)

total_amount = 0.0
validator_totals = defaultdict(float)
rows = []

with open(CSV_PATH, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        amount = float(row["amount"])
        total_amount += amount
        validator_totals[row["validator"]] += amount
        rows.append(row)

rows.sort(key=lambda r: datetime.strptime(r["date"], "%Y-%m-%d"))

print("=== Delegation Tracker Summary ===")
print()

print(f"Source CSV: {CSV_PATH}")
print(f"Total delegated amount: {total_amount}")
print()

print("By validator:")
for validator, amount in validator_totals.items():
    print(f"- {validator}: {amount}")

print()
print("Recent records:")
for row in rows[-5:]:
    print(f'- {row["date"]} | {row["validator"]} | {row["amount"]} | {row["note"]}')
