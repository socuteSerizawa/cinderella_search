from write_csv import CinderellaWriteCsv
from get_twitter import url, twitter
import json
import time

# Enedpointへ渡すパラメーター
keyword = 'Violet Violence exclude:retweets'

header = ['user_id', 'id', 'created_at', 'text']
cinderella_csv = CinderellaWriteCsv('./sample.csv', header)

MAX_ID = -1
SINCE_ID = -1
MAX_TWEETS_ONETIME = 100

params ={
         'count'   : MAX_TWEETS_ONETIME, # 取得するtweet数
         'q'       : keyword,    # 検索キーワード
         'max_id'  : MAX_ID,     # 取得する最大tweetID
         'since_id': SINCE_ID,   # このIDより大きいtweetIDを取得
         }

MAX_ROOP = 100

roop_count = 0
count_tweets_for_debug = 0
while(roop_count < MAX_ROOP):
	# リクエストクエリの送信
	req = twitter.get(url, params = params)

	if req.status_code == 200:
		res = json.loads(req.text)

		# 受信結果から，必要なカラムのピックアップ
		list_for_add_csv =[]
		for column_tweet in res['statuses']:
			dict_of_column = {}
			# tweet_id, created_at, textを取得
			for i in range(1, len(header)):
				dict_of_column[header[i]] = column_tweet[header[i]]
			# user_idを取得
			dict_of_column[header[0]] = column_tweet['user']['id'] 
			list_for_add_csv.append(dict_of_column)
			# 取得したtweet数の記録
			count_tweets_for_debug += 1
		# CSVに保存
		cinderella_csv.add_columns(list_for_add_csv)
		# 取得する最大tweet_idを更新
		params['max_id'] = list_for_add_csv[-1]['id'] - 1
		# 取得したtweet数の確認
		print(count_tweets_for_debug)
		# 受信結果数により，これ以上取得可能なtweetがあるかどうかを判定
		if(len(list_for_add_csv) < MAX_TWEETS_ONETIME):
			break

	else:
		print("Failed: %d" % req.status_code)

	roop_count += 1
	time.sleep(1)

print('record tweets = '+ str(count_tweets_for_debug))
