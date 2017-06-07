# -*- coding:utf8 -*-
import json
import codecs

def get_submission(result_filepath):
	
	f = open(result_filepath)
	f_new = codecs.open("./result/submission_tfidf_k23.txt",'w','utf8')
	
	for i,line in enumerate(f.readlines()):
		'''
		temp_dic = {}
		print type(line) , line
		line = line.decode("utf8")
		print type(line) , line
		temp_dic["summarization"] = line
		temp_dic["index"] = i
		js = json.dumps(temp_dic,ensure_ascii=False)
		print type(js),js
		js = js.decode("utf8")
		print type(js),js 
		#f_new.write(js)
		#f_new.write('\n')
		'''
	
		f_new.write('''{"summarization": "'''.decode("utf8"))
		f_new.write(line.strip().decode("utf8"))
		f_new.write('''", "index": '''.decode("utf8"))
		f_new.write(str(i).decode("utf8"))
		f_new.write("}".decode("utf8"))
		f_new.write('\n'.decode("utf8"))

	f.close()
	f_new.close()

if __name__ == '__main__':
	
	result_filepath = "./result/test_data_result_tfidf_k23.txt"
	get_submission(result_filepath)
