class KeywordFilter():
	keyword = ''
	def __init__(self, idol_name_list, exclude_retweet = True):
		self.add_keyword(idol_name_list[0])
		if len(idol_name_list) > 0:
			for word in range(1, len(idol_name_list)):
				self.add_keyword('OR')
				self.add_keyword(idol_name_list[word])

		if exclude_retweet == True:
			self.add_keyword('exclude:retweets')

	def add_keyword(self, add_word):
		self.keyword += ' '
		self.keyword += add_word