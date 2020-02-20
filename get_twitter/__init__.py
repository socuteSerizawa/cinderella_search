import get_twitter.config
from requests_oauthlib import OAuth1Session

# OAuth認証部分
CK      = config.CONSUMER_KEY
CS      = config.CONSUMER_SECRET
AT      = config.ACCESS_TOKEN
ATS     = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

# Twitter Endpoint(検索結果を取得する)
url = 'https://api.twitter.com/1.1/search/tweets.json'
