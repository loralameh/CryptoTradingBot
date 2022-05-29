import snscrape.modules.twitter as sntwitter
import pandas as pd

maxTweets = 1000

# Creating list to append tweet data to
tweets_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('#Mana ').get_items()):
    if i>maxTweets:
        break
    tweets_list.append([tweet.date,  tweet.content])

# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text'])

# Display first 5 entries from dataframe
tweets_df.head()

# Export dataframe into a CSV
tweets_df.to_csv('tweets.csv', sep=',', index=False)