#-*- coding:utf-8 -*-
from gensim import models,corpora
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

def get_index_of_summary(dic, model_tfidf, corpus_list, k, list_word):
	
	stopwords_list = get_stopwords_list()
	corpus_list = [word_tuple for word_tuple in corpus_list \
		if dic.get(word_tuple[0]) not in stopwords_list and not re.match("^\d*$",dic.get(word_tuple[0]))]
	k = len(list_word)/k

	list_max_k = get_max_k_tuple_list(model_tfidf[corpus_list],k)
	list_max_word = [dic.get(t[0]) for t in list_max_k]
	s = " ".join(list_word).replace("\n","")
	cal_list = []

	for i,sen in enumerate(re.split('，|。|：|；|？|！',s)):
		sen_list = sen.split(' ')
		temp_list = []
		temp_value = 0.0
		n = 0
		
		for j , word in enumerate(sen_list):
			if word.decode("utf8") in list_max_word:
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

def use_tfidf_cal_summary( test_filepath , result_filepath , k):
	
	
	dic = corpora.Dictionary.load("./model/dictionary.tfidf.dic")
	model_tfidf = models.TfidfModel.load("./model/tfidf_model")
	list_test_article = get_data.get_cut_data_list_list(test_filepath)
	corpus = [dic.doc2bow(text) for text in list_test_article]
	result_f = open(result_filepath,"w+")
	for i , tuple_list in enumerate(corpus):
		ans = get_index_of_summary(dic,model_tfidf,tuple_list,k,list_test_article[i])
		print i,ans
		result_f.write(ans+"\n")

	result_f.close()


if __name__ == "__main__":
	test_filepath = "./data/cut_article_test.txt"
	'''
	for k in range(5,16):
		result_filepath = "./result/EK_tfidf_result/0504_k=%d.txt"%(k)
		use_tfidf_cal_summary(test_filepath , result_filepath , k)
	
	for k in range(16,21):
		result_filepath = "./result/EK_tfidf_result/0504_k=%d.txt"%(k)
		use_tfidf_cal_summary(test_filepath , result_filepath , k)
	
	for k in range(21,26):
		result_filepath = "./result/EK_tfidf_result/0504_k=%d.txt"%(k)
		use_tfidf_cal_summary(test_filepath , result_filepath , k)
	'''
	for k in range(26,31):
		result_filepath = "./result/EK_tfidf_result/0504_k=%d.txt"%(k)
		use_tfidf_cal_summary(test_filepath , result_filepath , k)
