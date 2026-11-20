# Lab 3: The Social Media Data Detective

Analysis of a messy Twitter dataset (10,000 tweets) using custom Python algorithms and a Bash one-liner pipeline.

## Files

- `data-detective.py`: Python application (Quests 1 to 4)
- `feed-analyzer.sh`: Bash script that lists the Top 5 most active users
- `twitter_dataset.csv`: dataset (source: Kaggle, "Twitter Dataset" by goyaladi)
- `Readme.md`: this file

## Requirements

- Python 3 (on Windows, run it with `py`)
- Bash (Git Bash on Windows)
- No external libraries. The script only uses the standard library modules `csv`, `sys` and `os`, which come with Python and are part of the provided starter template.
- `.sort()`, `sorted()` and `max()` are not used anywhere.

## How to run

    py data-detective.py
    bash feed-analyzer.sh

On Linux or Mac, use `python3` instead of `py`. The script `feed-analyzer.sh` also accepts a custom file path:

    bash feed-analyzer.sh path/to/twitter_dataset.csv

## Python application

- **Quest 1, Data Auditor (`clean_data`)**: removes tweets with an empty `Text`, replaces an empty `Likes` or `Retweets` with 0, converts both to `int`, and prints how many rows were removed or fixed. On this dataset, 0 rows needed cleaning, but the function handles dirty data.
- **Quest 2, Viral Post (`find_viral_tweet`)**: a simple loop that keeps the tweet with the highest `Likes`. The comparison is strict (`>`), so when several tweets tie, the first one in the file is kept. 101 tweets have exactly 100 likes here, and the result is `ojordan`.
- **Quest 3, Custom Sort (`custom_sort_by_likes`)**: selection sort in descending order, working on a copy so the original list is unchanged. It runs in O(n²), so sorting 10,000 tweets takes a few seconds. Selection sort is not stable, so tied tweets may appear in a different order than in the file. The Top 10 is obtained by slicing `sorted_tweets[:10]`.
- **Quest 4, Content Filter (`search_tweets`)**: asks the user for a keyword (example: `health`), searches the `Text` field ignoring case, stores matches in a new list, and prints the number of matches with `len()`, followed by the tweets. An empty input shows an error message with an example.

## Shell script

`feed-analyzer.sh` extracts the usernames, counts them and prints the Top 5 most active users:

    awk -F',' 'NR > 1 && $1 ~ /^[0-9]+$/ {print $2}' twitter_dataset.csv | sort | uniq -c | sort -k1,1nr -k2,2 | head -n 5

The `Text` column contains line breaks inside quotes, so a plain `cut -d',' -f2` would count text fragments as usernames (about 25,775 lines instead of 10,000). The `awk` filter keeps only the lines that start a real record, meaning the first field is a number. It skips the header and the continuation lines. The script also checks that the file exists and prints a usage message if not.

## Error handling

- Missing or empty dataset: clear error message
- Empty search keyword: error message with an example
- Missing file passed to `feed-analyzer.sh`: error message and usage line
