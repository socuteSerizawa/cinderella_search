from write_csv import CinderellaWriteCsv
from get_twitter import url, twitter
import json

list_sample = []

list_sample.append({'a':10, 'b':20, 'c':30})
list_sample.append({'a':11, 'b':22, 'c':33})

cin_csv = CinderellaWriteCsv('./sample.csv', list_sample[0].keys())

cin_csv.add_columns(list_sample)

# Enedpointへ渡すパラメーター
keyword = '桐生つかさ exclude:retweets'

params ={
         'count' : 100,      # 取得するtweet数
         'q'     : keyword,  # 検索キーワード
         'max_id': None,     # 取得する最大tweetID
         }

req = twitter.get(url, params = params)

if req.status_code == 200:
	res = json.loads(req.text)
	for line in res['statuses']:
		print('id = ' + line['id_str'] + ' user_id = ' + line['user']['id_str'] + ' datetime = ' + line['created_at'])
		print(line['text'])
		print('*******************************************')
		
else:
	print("Failed: %d" % req.status_code)
