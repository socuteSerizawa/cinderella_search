from write_csv import CinderellaWriteCsv
from get_twitter import url, twitter
import json

# Enedpointへ渡すパラメーター
keyword = '桐生つかさ exclude:retweets'

header = ['user_id', 'id', 'created_at', 'text']
cinderella_csv = CinderellaWriteCsv('./sample.csv', header)

params ={
         'count' : 100,      # 取得するtweet数
         'q'     : keyword,  # 検索キーワード
         'max_id': None,     # 取得する最大tweetID
         }

req = twitter.get(url, params = params)

if req.status_code == 200:
	res = json.loads(req.text)
	list_for_add_csv =[]
	for line in res['statuses']:
		dict_of_column = {}
		# tweet_id, created_at, textを取得
		for i in range(1, len(header)):
			dict_of_column[header[i]] = line[header[i]]
		# user_idを取得
		dict_of_column[header[0]] = line['user']['id'] 
		list_for_add_csv.append(dict_of_column)

	cinderella_csv.add_columns(list_for_add_csv)

else:
	print("Failed: %d" % req.status_code)
