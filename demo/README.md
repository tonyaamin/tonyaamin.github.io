# Data Integrity Lab — Multi-Source Reconciliation

**Author:** Tonya Amin, MBA  
**Portfolio:** https://tonyaamin.github.io/  
**Data:** 100% synthetic; no actual ATLASARI, family, legal, employer, or client information.

## Business question
How can analysts detect duplicate, incomplete, and conflicting records received from multiple source systems without losing the original evidence trail?

## Methods
- Generate and inspect 219 fictional source records.
- Group on `event_key` to identify repeated logical events.
- Compare timestamps, amounts, and statuses to distinguish matching duplicates from conflicts.
- Flag missing required fields and create a review queue.
- Preserve every raw source record instead of silently overwriting conflicting values.

## Reproduce
From this directory, run `python analyze.py` (Python 3, no packages required). The CSV is provided alongside the script. SQL examples are written for SQLite; import the CSV as table `records` first.

## Scope and limitations
This is an illustrative portfolio case study, not an operational system or a claim of measured outcomes from real data. Duplicate event keys do not automatically mean records should be deleted. Conflicting values require human review and documented resolution rules. The sample dashboard is static and does not execute SQL or Python in the browser.

## Findings and implications
The 219 source rows represent 192 event keys. Twenty-three event keys appear in multiple rows; nine event keys have conflicting values across rows; eight rows have missing required timestamps or amounts. These are overlapping classifications, not additive totals. Potential impacts include distorted event counts, inconsistent reporting, and incomplete downstream calculations. No actual losses or operational savings are claimed.

## Review and prioritization
The sample queue marks conflicts and missing required values as High. Repeated keys with matching values require reconciliation but do not necessarily indicate errors. This priority assignment is a documented illustration, not a computed risk score in the scripts. Retain source-level records and document adjudication before deriving authoritative event values.

## Tools demonstrated
Python standard library (`csv`, `collections`, `pathlib`); SQLite-compatible SQL with `GROUP BY`, `HAVING`, `COUNT(DISTINCT)`, `COALESCE`, and `TRIM`; static HTML/CSS report.
