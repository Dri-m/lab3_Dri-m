import csv
import sys
import os

def load_raw_data(filename):
    """
    Loads the CSV file into a list of dictionaries exactly as it is (messy).
    """
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    raw_tweets = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            raw_tweets.append(row)
            
    return raw_tweets

def clean_data(tweets):
    """
    QUEST 1: Handle missing fields.
    Remove tweets with no Text, replace empty/invalid Likes or Retweets with 0.
    Likes and Retweets are converted to int so they can be compared later.
    Returns a clean list of tweets.
    """
    clean_tweets = []
    removed_count = 0
    fixed_count = 0

    for tweet in tweets:
        text = (tweet.get("Text") or "").strip()
        if text == "":
            removed_count += 1
            continue

        tweet["Text"] = text
        row_fixed = False

        for field in ("Likes", "Retweets"):
            value = (tweet.get(field) or "").strip()
            try:
                tweet[field] = int(value)
            except ValueError:
                tweet[field] = 0
                row_fixed = True

        if row_fixed:
            fixed_count += 1
        clean_tweets.append(tweet)

    print(f"Data audit: {removed_count} rows removed (missing Text), "
          f"{fixed_count} rows fixed (missing Likes/Retweets set to 0).")
    return clean_tweets

def find_viral_tweet(tweets):
    """
    QUEST 2: Loop through the list to find the tweet with the highest 'Likes'.
    Do not use the max() function.
    Expects cleaned data (Likes already converted to int by clean_data).
    """
    if len(tweets) == 0:
        print("Error: no tweets to analyze. Check that the dataset is not empty.")
        return None

    viral = tweets[0]
    for tweet in tweets:
        if tweet["Likes"] > viral["Likes"]:
            viral = tweet

    print("--- Most viral tweet ---")
    print(f"Username: {viral['Username']}")
    print(f"Likes:    {viral['Likes']}")
    print(f"Text:     {viral['Text']}\n")
    return viral

def custom_sort_by_likes(tweets):
    """
    QUEST 3: Implement Bubble Sort or Selection Sort to sort the list 
    by 'Likes' in descending order. NO .sort() allowed!
    """
    pass

def search_tweets(tweets, keyword):
    """
    QUEST 4: Search for a keyword and extract matching tweets into a new list.
    """
    pass

if __name__ == "__main__":
    # Load the messy data
    dataset = load_raw_data("twitter_dataset.csv")
    print(f"Loaded {len(dataset)} raw tweets.\n")

    # Call your functions here to complete the quests!
    clean_dataset = clean_data(dataset)
    print(f"{len(clean_dataset)} tweets remain after cleaning.\n")
    viral_tweet = find_viral_tweet(clean_dataset)