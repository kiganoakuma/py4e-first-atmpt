import tweepy

consumer_key = '1DFGQ9QHjpx7gtQLmN0KKvGK9'
consumer_secret = 'cbR352DrmUkVjBGWbwgL2AyjmmXlI4qBvuJnUXJl5ixVRdoJLr'
access_token = '1244186010558193664-xWT71aHFv2cOyt6R8fgHHp2OBZE2c8'
access_token_secret = 'uIMMKr5KZuLzLbiF8U5Gkos9f8n8k4yDgDt4PwDq77mjC'


# Authenticate with Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Prompt the user to enter a Twitter username
username = input("Enter a Twitter username: ")

try:
    # Retrieve the user's timeline tweets
    tweets = api.user_timeline(screen_name=username, count=10)

    # Print the last 10 tweets
    print(f"Last 10 tweets from {username}:")
    for tweet in tweets:
        print(tweet.text)
        print("-" * 30)

except tweepy.TweepError as e:
    print(f"Error: {e}")
