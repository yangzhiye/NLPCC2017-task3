# -*- encoding:utf-8 -*-

import codecs
from textrank4zh import TextRank4Keyword , TextRank4Sentence

text = "这间酒店位于北京东三环，里面摆着很多雕塑，文艺气息十足。答谢宴于晚上８点开始。"
print type(text)
tr4w = TextRank4Keyword()

tr4w.analyze(text = text , lower = True , window = 2)

for s in tr4w.sentences:
	print s


print ('words_no_filter')
for words in tr4w.words_no_filter:
	print ('/'.join(words))

print ('words_no_stop_words')
for words in tr4w.words_no_stop_words:
	print ('/'.join(words))

print ('words_all_filters')
for words in tr4w.words_all_filters:
	print ('/'.join(words))

print ('keywords')
for item in tr4w.get_keywords(20,word_min_len = 1):
	print  ''.join(item.word) , item.weight

print ('key short phrases')
for phrase in tr4w.get_keyphrases(keywords_num = 20 , min_occur_num = 1):
	print phrase

tr4s = TextRank4Sentence()

tr4s.analyze(text = text , lower = True , source = 'all_filters')

print "summary"
for item in tr4s.get_key_sentences(num = 2):
	print item.index,item.weight,''.join(item.sentence)
