#!/bin/bash
# feed-analyzer.sh - Top 5 most active users in twitter_dataset.csv
# Usage: ./feed-analyzer.sh [path/to/twitter_dataset.csv]

FILE="${1:-twitter_dataset.csv}"

if [ ! -f "$FILE" ]; then
    echo "Error: file '$FILE' not found." >&2
    echo "Usage: ./feed-analyzer.sh twitter_dataset.csv" >&2
    exit 1
fi

echo "--- Top 5 Most Active Users ---"

# 1. awk keeps only real record lines (first field is a number, which skips the
#    header and the continuation lines of multi-line tweets) and prints Username.
# 2. sort groups identical usernames together.
# 3. uniq -c counts each username.
# 4. sort -k1,1nr -k2,2 orders by highest count (ties broken alphabetically).
# 5. head keeps the first 5.
awk -F',' 'NR > 1 && $1 ~ /^[0-9]+$/ {print $2}' "$FILE" \
    | sort \
    | uniq -c \
    | sort -k1,1nr -k2,2 \
    | head -n 5
