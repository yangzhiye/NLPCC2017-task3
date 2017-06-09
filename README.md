# NLPCC 2017 task3

## 基础方法

### 提取关键词/句子法计算文本摘要

#### tfidf提取关键词计算文本摘要 [论文地址](http://www.di.ubi.pt/~jpaulo/competence/general/(1958)Luhn.pdf)

#### 结果
![](https://github.com/yangzhiye/ImageCache/blob/master/NLPCC%20task3/nlpcc_tfidf_k25.png)

#### textrank提取关键词/句方法计算文本摘要 [论文地址](http://www.aclweb.org/anthology/W/W04/W04-3252.pdf)

#### 结果
![](https://github.com/yangzhiye/ImageCache/blob/master/NLPCC%20task3/nlpcc_textrank.png)

## 评价指标

1.ROUGE1&2 ROUGE SU4 R&F(ROUGE.py) [论文地址](http://www.aclweb.org/anthology/W04-1013)

## 文本摘要调研

### 论文调研

#### The Automatic Creation of Lierature Abstracts [论文地址](http://courses.ischool.berkeley.edu/i256/f06/papers/luhn58.pdf)

1. TFIDF计算关键词->通过关键词的密集程度计算关键句->通过关键句形成摘要

#### TextRank:Bringing Order into Texts [论文地址](http://www.aclweb.org/anthology/W/W04/W04-3252.pdf)

1. 使用Textrank方法提取文本中关键词/句

## 最终结果
![](https://github.com/yangzhiye/ImageCache/blob/master/NLPCC%20task3/nlpcc.png)

排名5/9。。溜了溜了。。实习去了。。明年再战。。。