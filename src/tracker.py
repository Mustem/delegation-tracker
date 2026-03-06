import csv
from collections import defaultdict
from datetime import datetime

CSV_PATH = "data/delegations.csv"

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

print(f"Total delegated amount: {total_amount}")
print()

print("By validator:")
for validator, amount in validator_totals.items():
    print(f"- {validator}: {amount}")

print()
print("Recent records:")
for row in rows[-5:]:
    print(f'- {row["date"]} | {row["validator"]} | {row["amount"]} | {row["note"]}')
