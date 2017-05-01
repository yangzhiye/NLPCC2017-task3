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
	for i,line in enumerate(f.readlines())
		stopwords_list.append(line.decode("utf8"))
	f.close()

def get_index_of_summary(dic, model_tfidf, corpus_list, k, list_word):
	


def use_tfidf_cal_summary( test_filepath , result_filepath , k):
	

	dic = corpora.Dictionary.load("./model/dictionary.tfidf.dic")
	model_tfidf = models.TfidfModel.load("./model/tfidf_model")

