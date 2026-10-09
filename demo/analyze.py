"""Reproducible data-quality audit using only Python standard library."""
import csv
from collections import defaultdict, Counter
from pathlib import Path

path = Path(__file__).with_name("synthetic_records.csv")
with path.open(newline="", encoding="utf-8") as handle:
    rows = list(csv.DictReader(handle))

by_key = defaultdict(list)
for row in rows:
    by_key[row["event_key"]].append(row)

duplicate_keys = {key for key, group in by_key.items() if len(group) > 1}
conflicting_keys = {
    key for key, group in by_key.items()
    if len({(r["event_time"], r["amount"], r["status"]) for r in group}) > 1
}
missing_rows = [r for r in rows if not r["event_time"] or not r["amount"]]

print("Records:", len(rows))
print("Distinct event keys:", len(by_key))
print("Duplicate event keys:", len(duplicate_keys))
print("Conflicting event keys:", len(conflicting_keys))
print("Rows missing required fields:", len(missing_rows))
print("By source:", dict(Counter(r["source"] for r in rows)))

assert len(rows) == 219
assert len(by_key) == 192
assert len(duplicate_keys) == 23
assert len(conflicting_keys) == 9
assert len(missing_rows) == 8
