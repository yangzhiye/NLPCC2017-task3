# -*- encoding:utf-8 -*-

from snownlp import SnowNLP


text = u'这间酒店位于北京东三环，里面摆着很多雕塑，文艺气息十足。答谢宴于晚上８点开始。'

s = SnowNLP(text)

print ' '.join(s.keywords(3))

print ' '.join(s.summary(3))


