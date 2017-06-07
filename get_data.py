#*- coding: utf-8 -*-
import re
import thulac

def parser_and_return_data_list(filepath):
	
	f = open(filepath)
	list_summarization = []
	list_article = []
	for i,line in enumerate(f.readlines()):
		temp_dic = eval(line) # eval:line to dic
		list_summarization.append(temp_dic["summarization"])
		list_article.append(temp_dic["article"])
	
	return list_summarization , list_article


def get_clean_data_list(filepath):
	
	list_summarization , list_article = parser_and_return_data_list(filepath) 
	
	def _remove_special_char(m):
		s = m.group(0)
		if s in u'，。！？；：“”《》':
			return s
		return ''
	
	for i,line in enumerate(list_summarization):
		line = line.decode("utf8")
		list_summarization[i] = re.sub(u'[^\u4e00-\u9fa50-9a-zA-Z]',\
		_remove_special_char,line)
	
	for i,line in enumerate(list_article):
		line = line.decode("utf8")
		line = re.sub(u'<Paragraph>','',line)
		list_article[i] = re.sub(u'[^\u4e00-\u9fa50-9a-zA-Z]',\
		_remove_special_char,line)
	
	return list_summarization , list_article
	
def write_cut_word_to_file():
	
	filepath_summ = "./data/train_with_summ.txt"
	filepath_no_summ = "./data/train_without_summ.txt"
	
	_,list_article = get_clean_data_list(filepath_summ)  #50000 unicode
	_,list_no_summ_article = get_clean_data_list(filepath_no_summ)  #50000 unicode
	
	f_article = open("./data/cut_article.txt","w+")
	f_no_summ_article = open("./data/cut_no_summ_article.txt","w+")

	thu_cut = thulac.thulac("-seg_only")

	for i,article in enumerate(list_article):
		article = article.encode("utf8")
		list_temp = thu_cut.cut(article)
		try:
			content = " ".join(list_temp)
		except:
			print i
			content = "wrong context"
		f_article.write(content+"\n")
	f_article.close()
	
	for i,article in enumerate(list_no_summ_article):
		article = article.encode("utf8")
		try:
			list_temp = thu_cut.cut(article)
			content = " ".join(list_temp)
		except:
			print i
			content = "wrong context"
		f_no_summ_article.write(content+"\n")
	f_no_summ_article.close()

def write_test_cut_word_to_file():
	
	thu_cut = thulac.thulac("-seg_only")
	filepath_test_data = "./data/test_data/evaluation_without_ground_truth.txt"
	_,list_test_data = get_clean_data_list(filepath_test_data)
	f_test_data = open("./data/test_data/cut_test.txt","w+")
	for i,article in enumerate(list_test_data):
		article = article.encode("utf8")
		list_temp = thu_cut.cut(article)
		content = " ".join(list_temp)
		f_test_data.write(content+"\n")
	f_test_data.close()

def get_all_cut_short_text():
	
	f_article = open("./data/cut_article.txt",'r')
	f_no_summ_article = open("./data/cut_no_summ_article.txt",'r')
	f_test = open("./data/test_data/cut_test.txt")
	list_cut_short_text = []

	for i,line in enumerate(f_article):
		temp_list = line.split(' ')
		list_cut_short_text.append(temp_list)
	#print len(list_cut_short_text)
	for i,line in enumerate(f_no_summ_article):
		temp_list = line.split(' ')
		list_cut_short_text.append(temp_list)
	for i,line in enumerate(f_test):
		temp_list = line.split(' ')
		list_cut_short_text.append(temp_list)
	#print len(list_cut_short_text)
	return list_cut_short_text

def division_train_and_test_data():
	
	filepath = './data/cut_article.txt'
	f_article = open(filepath,'r')
	
	f_new_train = open("./data/cut_article_train.txt",'w+')
	f_new_test = open("./data/cut_article_test.txt",'w+')
	
	for i,line in enumerate(f_article):
		if i < 45000:
			f_new_train.write(line)
		if i >= 45000:
			f_new_test.write(line)
	
	f_article.cloee()
	f_new_train.close()
	f_new_test.close()

def get_cut_data_list_list(filepath):
	
	list_article = open(filepath,'r')
	
	list_test_article = []

	for i , line in enumerate(list_article):
		
		list_test_article.append(line.split(" "))

	return list_test_article
	
def get_test_summary():

	list_summary , _ = parser_and_return_data_list("data/train_with_summ.txt")

	return list_summary[45000:]

if __name__ == '__main__':
	
	#get_clean_data_list("data/train_with_summ.txt")
	#write_cut_word_to_file()
	#get_all_cut_short_text()
	#division_train_and_test_data()
	#list_test_article = get_cut_data_list_list("./data/cut_article_test.txt")
	#print len(list_test_article) ,type(list_test_article[0]) ,list_test_article[0]
	#list = get_test_summary()
	write_test_cut_word_to_file()




