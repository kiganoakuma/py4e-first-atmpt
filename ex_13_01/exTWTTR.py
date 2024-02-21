
import tweepy

bearer_token = 'AAAAAAAAAAAAAAAAAAAAAApDrQEAAAAA1%2B1P6QM2RIMjIC6S5g1JrNae2Rk%3DbvedIuXhmgCRUpNkIcDMSrJUKuhZjT3DrrTsTWNt8tR8a13ha2'
consumer_token = '5DTsHoY7CAyu3mI57KDkDWmzw'
consumer_secret = 'vzeOP0ELia5oP4VDJRBCQC50tObmfAQpAFjn8xE1wLOrw8wpoJb'
access_token = '1244186010558193664-wTq0Xv5zEWJ4Nj0y1FPArb3Lzw4DAS'
access_token_secret = '0PgzQUPZxWq0kGLwYQup1AN4L4Rjn5KfY5c93MfCxbOrC'

client = tweepy.Client(bearer_token=bearer_token)

client = tweepy.Client(
    consumer_token=consumer_token, consumer_secret=consumer_secret,
    access_token=access_token, access_token_secret=access_token_secret
)
tweets = client.get_all_tweets_count

print(tweets)
