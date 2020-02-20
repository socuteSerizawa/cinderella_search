import csv

class CinderellaWriteCsv():
	def __init__(self, filepath, list_header):
		self.filepath = filepath
		self.header = list_header
		with open(self.filepath, 'w') as f:
			writer = csv.DictWriter(f, self.header)
			writer.writeheader()

	def add_columns(self, list_tweets):
		with open(self.filepath, 'a') as f:
			writer = csv.DictWriter(f, self.header)
			for line in list_tweets:
				writer.writerow(line)