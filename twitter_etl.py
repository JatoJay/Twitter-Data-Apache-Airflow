import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs


access_key = "5xRNG4diG3G9tL9xiurmOreZ4"
access_secret = "yW1Of7JHDStNhE1P8c7U0pwqtGwP0To2bRnvD7VZVncooeFOgf"
consumer_key = "754072515228606464-aoTejOU039nnoo9rzNEJ1wViyzIl2Lk"
consumer_secret = "VTD7rryKtdsUqIqlnps4m4yDIaypQRtAQZkL2q9IPKDoL"


# Twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)   
auth.set_access_token(consumer_key, consumer_secret) 

# # # Creating an API object 
api = tweepy.API(auth)
tweets = api.user_timeline(screen_name='@elonmusk', 
                            # 200 is the maximum allowed count
                            count=20,
                            include_rts = False,
                            # Necessary to keep full_text 
                            # otherwise only the first 140 words are extracted
                            tweet_mode = 'extended')
print(tweets)