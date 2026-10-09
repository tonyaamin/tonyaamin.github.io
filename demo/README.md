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
