import snscrape.modules.twitter as sntwitter
import pandas as pd

maxTweets = 10000

# Creating list to append tweet data to
tweets_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('#mana  since:2022-03-01 until:2022-04-08').get_items()):
    if i>maxTweets:
        break
    tweets_list.append([tweet.date,  tweet.content])
    print(i)

# Creating a dataframe from the tweets list above
tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Text'])

# Display first 5 entries from dataframe
tweets_df.head()

# Export dataframe into a CSV
tweets_df.to_csv('tweetsMarch.csv', sep=',', index=False)
