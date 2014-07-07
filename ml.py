import Quandl
import numpy
from monthloop import scrape
from test import urlsum
import numpy as np
import glob
import os
## Text Summarizing Library ##
#from __future__ import absolute_import
#from __future__ import division, print_function, unicode_literals

from sumy.parsers.html import HtmlParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


## Sentiment Analysis Library ##
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
## Machine Learning and metrics ##
from sklearn import svm
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from itertools import islice

def ml(query, name):
	#name = "GOOG/NASDAQ_AAPL"
	mydata = Quandl.get(name, authtoken="P4XxRkeVJCEmXmzJuESv", trim_start="2014-03-01", trim_end="2014-03-31", returns="numpy")
#	print np.shape(mydata)
	## Grabbing data
	#grab = scrape(query)
	
	## Find correlating stock date
	stockdates = [str(i[0]) for i in mydata]
	
	openp = [str(i[1]) for i in mydata]

	high = [str(i[2]) for i in mydata]	

	low = [str(i[3]) for i in mydata]

	close = [str(i[4]) for i in mydata]
	
	changes = []
	for i in close:
		for j in openp:
			cf = ((float(i) - float(j)) / (float(j))) 
			changes.append(cf)
        X = np.empty([6,1])

#        y = np.empty([1,1])
	
	statc = []

	for entry, change in zip(stockdates, changes):
		
		#dayval = entry[-2:]
		#sd = (dayval, altd)
		#print dayval 
		
		### Financial ###
		'''
		open = [str(i[1]) for i in mydata]
	
        	high = [str(i[2]) for i in mydata]
	
        	low = [str(i[3]) for i in mydata]
	
        	close = [str(i[4]) for i in mydata]
	
	        change = ((int(close) - int(open)) / (int(open)))
		'''
		
		#labdict = []
		'''
		for i in mydata:
			openp = str(i[1])

        	        high = str(i[2])
	
        	        low = str(i[3])
	
        	        close = str(i[4])
	
        	        change = ((float(close) - float(openp)) / (float(openp)))
			#cht = str(change)
			#labdict.append(str(cht))
#			y = np.append(change,y)
		 '''
		label = query + 'lab.txt'			
		#labelfile = open(label, 'w+')
		#labelfile.write(labdict)
		#######################
#		statc = [] # change in price % 
		search = query.split(' ', 1)[0] + '.txt'
		datafiles = glob.glob(search)
		matching = [s for s in datafiles if entry in s]
		#print(matching)
		
		for item in matching:
			
    			### Just opening the file, still same error##
			#linkfile = open(item, 'r')
			### First 5 lines of file opening ##
			with open(item) as f:
				e = list(f)
				g = list(set(e))
           			file = list(islice(g,0,10,1))
				print file
			#x = 1 #first 4 articles
			for link in file:
	
				listp = urlsum(link, 10) # Summary
				
				if listp == 'exception':
					continue
				else:
					
					if len(listp) < 3:
						print('lack of data')
					else:
						
						
						### Extracting sentences and putting into strings ##
						b1 = unicode(listp[0])
						b2 = unicode(listp[1])
						b3 = unicode(listp[2])
						
						blob1 = TextBlob(b1, analyzer = NaiveBayesAnalyzer())
						blob2 = TextBlob(b2, analyzer = NaiveBayesAnalyzer())
						blob3 = TextBlob(b3, analyzer = NaiveBayesAnalyzer())
						
						blobt1 = TextBlob(b1)
						blobt2 = TextBlob(b2)
						blobt3 = TextBlob(b3)
						
						#Polarity, subjectivity, p_pos, p_neg
						print('sentiment-polarity')
						print(blobt1.sentiment.polarity)
						print(blobt2.sentiment.polarity)
						print(blobt3.sentiment.polarity)
						print('sentiment-subjectivity')
						print(blobt1.sentiment.subjectivity)
                				print(blobt2.sentiment.subjectivity)
                				print(blobt3.sentiment.subjectivity)
						print('sentiment-p_pos')
						print(blob1.sentiment.p_pos)
						print(blob2.sentiment.p_pos)
						print(blob3.sentiment.p_pos)
						print('sentiment-p_neg')
                				print(blob1.sentiment.p_neg)
                				print(blob2.sentiment.p_neg)
                				print(blob3.sentiment.p_neg)
						print('next article')					
	
		
						print('sentiment-polarity')
                                        	'''
						aa = (blobt1.sentiment.polarity)
                                        	ba = (blobt2.sentiment.polarity)
                                        	ca = (blobt3.sentiment.polarity)
                                        	da = ('sentiment-subjectivity')
                                        	ea = (blobt1.sentiment.subjectivity)
                                        	fa = (blobt2.sentiment.subjectivity)
                                        	ga = (blobt3.sentiment.subjectivity)
                                        	'''
						ha = ('sentiment-p_pos')
                                        	ia = (blob1.sentiment.p_pos)
                                        	ja = (blob2.sentiment.p_pos)
                                        	ka = (blob3.sentiment.p_pos)
                                        	la = ('sentiment-p_neg')
                                        	ma = (blob1.sentiment.p_neg)
                                        	na = (blob2.sentiment.p_neg)
                                        	oa = (blob3.sentiment.p_neg)
                                        	pa = ('next article')
						
						statc.append(change)
						sample = np.vstack((ia,ja,ka,ma,na,oa))
						#X = empty([1,12])
						X = np.append(X, sample, axis=1)
						xy = X.shape
						print(xy)
						print(change)
						print(X)
						print(statc)
			#			y = np.concatenate((change,sample), axis=1)		
						
							
							
							
		
	Xd = X[:,1:].T
	lb = np.array(statc)
	datums = query + 'data.txt'
	np.savetxt(datums, Xd)
	np.savetxt(label, lb)
	#return X
	#return y
	n_samples = len(statc)
	clf = svm.SVR()
	clf.fit(Xd[:n_samples / 1.25], lb[:n_samples / 1.25])
	expected = lb[n_samples / .8:]
	predicted = clf.predict(lb[n_samples / .8:])
	print(explained_variance_score(expected, predicted))
	print(mean_absolute_error(expected, predicted))
	print(mean_squared_error(expected, predicted))
	print(r2_score(expected, predicted))
	
	
ml("Apple","GOOG/NASDAQ_AAPL")
