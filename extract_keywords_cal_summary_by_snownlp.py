
#-*- coding:utf-8 -*-
from gensim import models,corpora
from textrank4zh import TextRank4Keyword
from snownlp import SnowNLP
import get_data
import re
import heapq


def get_max_k_tuple_list (tuple_list , k):
	
	return heapq.nlargest(k , tuple_list , key = lambda x : x[1])

def get_stopwords_list():
	filepath = "./stopword.txt"
	f = open(filepath)
	stopwords_list = []
	for i,line in enumerate(f.readlines()):
		stopwords_list.append(line.decode("utf8"))
	f.close()

	return stopwords_list

def get_index_of_summary(article,k):

	list_word = article
	k = len(article)/k
	article = ''.join(article)
	s = SnowNLP(article.decode("utf8"))
	keyword_list = s.keywords(k)

	s = " ".join(list_word).replace("\n","")
	cal_list = []

	for i,sen in enumerate(re.split('，|。|：|；|？|！',s)):
		sen_list = sen.split(' ')
		temp_list = []
		temp_value = 0.0
		n = 0
		
		for j , word in enumerate(sen_list):
			if word in keyword_list:
				temp_list.insert(j,1)
			else:
				temp_list.insert(j,0)
		length = 0
		for k in temp_list:
			length += 1
			if k==1:
				n += 1
		try:
			temp_value = n*n*1.0/length
		except:
			temp_value = 0
		sen = ''.join(sen.split())
		sen = re.sub("\d{4,}",'',sen)
		cal_list.append((i,temp_value,sen))

	cal_list = sorted(cal_list,key=lambda x : (-x[1],x[0]))
	
	all_size = 0
	ans_list = []
	for t in cal_list:
		if all_size+len(t[2].decode("utf8"))+1 <= 60 and t[1]>0:
			ans_list.append(t)
			all_size+=(len(t[2].decode("utf8"))+1)

	ans_list = sorted(ans_list,key=lambda x : (x[0]))
	ans = ""
	for i,t in enumerate(ans_list):
		if i == len(ans_list)-1:
			ans+=t[2]
			ans+="。"
		else:
			ans+=t[2]
			ans+="，"
	return ans

def use_snownlp_cal_summary( test_filepath , result_filepath , k):
	
	list_test_article = get_data.get_cut_data_list_list(test_filepath)
	result_f = open(result_filepath,"w+")
	for i , article in enumerate(list_test_article):
		ans = get_index_of_summary(article , k)
		print i,ans
		result_f.write(ans+"\n")

	result_f.close()


if __name__ == "__main__":
	test_filepath = "./data/cut_article_test.txt"
	
	for k in range(10,20):
		result_filepath = "./result/EK_snownlp_result/0521_k=%d.txt"%(k)
		use_snownlp_cal_summary(test_filepath , result_filepath , k)
