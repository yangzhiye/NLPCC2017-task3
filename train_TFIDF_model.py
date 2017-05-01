import get_data
import logging
from gensim import models,corpora

def train_TFIDF():
	
	list_cut_article = get_data.get_all_cut_short_text()

	logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level = logging.INFO)

	dictionary = corpora.Dictionary(list_cut_article)

	dictionary.save("dictionary.tfidf.dic")

	corpus = [dictionary.doc2bow(text) for text in list_cut_article]

	tfidf = models.TfidfModel(corpus)

	tfidf.save('./model/tfidf_model')

if __name__ == "__main__":
	
	train_TFIDF()


