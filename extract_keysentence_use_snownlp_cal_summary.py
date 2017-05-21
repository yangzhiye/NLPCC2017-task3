
# -*- encoding:utf-8 -*-
import codecs
from snownlp import SnowNLP
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
		s = SnowNLP(article.decode('utf8'))
		keysentence_list = s.summary(20)
		keysentence_list = [ks.encode("utf8") for ks in keysentence_list]

		result = ""
		for j , sentence in enumerate(keysentence_list):
			sentence = re.sub('\d{4,}','',sentence).decode("utf8")
			if j == 0 and len(sentence) > 59:
				result = sentence[:59]
				result += u"。"
				break
			if (len(result) + len(sentence)) <= 59:
				result += sentence
				result += u"，"
			else:
				break
		#print type(result)
		
		if result[-1] == u"，":
			result = result[:-2] + u"。"
		result_list.append(result)
		print i,result

	return result_list

def write_result_to_file():
	result_list = cal_summary()
	
	result_f = open("./result/ES_snownlp_result/0520.txt","w+")
	for i,summary in enumerate(result_list):
		#print i , summary
		result_f.write(summary.encode("utf8")+"\n")
	result_f.close()
	

if __name__ == '__main__':
	write_result_to_file()
