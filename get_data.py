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

def get_all_cut_short_text():
	
	f_article = open("./data/cut_article.txt",'r')
	f_no_summ_article = open("./data/cut_no_summ_article.txt",'r')
	list_cut_short_text = []

	for i,line in enumerate(f_article):
		temp_list = line.split(' ')
		list_cut_short_text.append(temp_list)
	#print len(list_cut_short_text)
	for i,line in enumerate(f_no_summ_article):
		temp_list = line.split(' ')
		list_cut_short_text.append(temp_list)

	#print len(list_cut_short_text)
	return list_cut_short_text


if __name__ == '__main__':
	
	#get_clean_data_list("data/train_with_summ.txt")
	#write_cut_word_to_file()
	get_all_cut_short_text()

