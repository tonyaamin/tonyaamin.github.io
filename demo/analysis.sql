-- SQLite examples: import synthetic_records.csv as table records.
-- All data is fictional. Never substitute private source material.

-- Source volume
SELECT source, COUNT(*) AS record_count
FROM records GROUP BY source ORDER BY source;

-- Event keys appearing in multiple source rows
SELECT event_key, COUNT(*) AS occurrence_count,
       COUNT(DISTINCT source) AS source_count
FROM records GROUP BY event_key HAVING COUNT(*) > 1
ORDER BY occurrence_count DESC, event_key;

-- Missing required values
SELECT record_id, event_key, source
FROM records WHERE amount IS NULL OR TRIM(amount) = ''
   OR event_time IS NULL OR TRIM(event_time) = '';

-- Conflicting amounts or timestamps among same-key records
SELECT event_key, COUNT(*) AS rows_per_key
FROM records GROUP BY event_key
HAVING COUNT(DISTINCT COALESCE(amount, '')) > 1
    OR COUNT(DISTINCT COALESCE(event_time, '')) > 1
    OR COUNT(DISTINCT COALESCE(status, '')) > 1;
