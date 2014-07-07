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
##
## function and unpacking ##
#from sys import argv
#script, url, SENTENCES_COUNT = argv

### Some TextBlob tests ##
'''
testimonial = TextBlob("Kaushik is generally a very good boy")
print "NON-nltk"
print testimonial.sentiment
print testimonial.polarity

print "NLTK-analyzer"
blob = TextBlob("Kaushik is generally a very good boy", analyzer = NaiveBayesAnalyzer())
print blob.sentiment
'''
LANGUAGE = "english"
########################################################################
### Testing out Sumy url capture ###

def urlsum(url, SENTENCES_COUNT): 
	try:
		parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
	except:
		return('exception')
	else:
		stemmer = Stemmer(LANGUAGE)
		
		summarizer = Summarizer(stemmer)
		summarizer.stop_words = get_stop_words(LANGUAGE)
		
		
		## Store Sentences ##
		firstlast = []
		## Print out summarized sentences ##
		for sentence in summarizer(parser.document, SENTENCES_COUNT):
			firstlast.append(sentence) ## save it to a list
			
	#	print(firstlast[0])
	#	print(firstlast[1])
	#	print(firstlast[-1])
		return firstlast
		
########################################################################


'''
### Testing ###
#url = "http://www.forbes.com/sites/amitchowdhry/2014/03/18/facebooks-deepface-software-can-match-faces-with-97-25-accuracy/"
list = urlsum(url, SENTENCES_COUNT)

### Extracting sentences and putting into strings ##
b1 = unicode(list[0])
b2 = unicode(list[1])
b3 = unicode(list[2])

blob1 = TextBlob(b1, analyzer = NaiveBayesAnalyzer())
blob2 = TextBlob(b2, analyzer = NaiveBayesAnalyzer())
blob3 = TextBlob(b3, analyzer = NaiveBayesAnalyzer())

print(blob1.polarity)
print(blob2.polarity)
print(blob3.polarity)

print(blob1.sentiment)
print(blob2.sentiment)
print(blob3.sentiment)
'''
