# -*- encoding:utf-8 -*-
import codecs
from textrank4zh import TextRank4Sentence
import re


def get_test_article_list():
	article_list = []
	f = open('./data/cut_article_test.txt','r')
	for i,line in enumerate(f):
		article_list.append(''.join(line).replace(' ',''))
	return article_list

def cal_summary():
	article_list = get_test_article_list()
	result_list = []

	for i , article in enumerate(article_list):
	
		tr4s = TextRank4Sentence()
		tr4s.analyze(text = article , lower = True , source = 'all_filters')
		keysentence_list = []
		for item in tr4s.get_key_sentences(num = 10):
			s = ''.join(item.sentence)
			s = re.sub("\d{4,}",'',s)
			keysentence_list.append(s)
		result = ""
		for j , sentence in enumerate(keysentence_list):
			print sentence , len(sentence) , type(sentence)
			break
			if j == 0 and len(sentence) > 60:
				result = sentence[:60]
				break
			if (len(result) + len(sentence)) <= 60:
				result += sentence
			else:
				break
		result_list.append(result)

	return result_list

def write_result_to_file():
	result_list = cal_summary()
	result_f = open("./result/ES_textrank4zh_result/0518.txt","w+")
	for i,summary in enumerate(result_list):
		print i , summary
		result_f.write(summary+"\n")
	result_f.close()

if __name__ == '__main__':
	write_result_to_file()
