from TagPhrase import getTagPhrase
import CreateLexicon as cl 
import SentimentValue as sv
import SentencePolarity as sp

def getSentimentAnalysis(line, trainpath = './data'):
	obj = cl.CreateLexicon(trainpath)
	all_text_ = getTagPhrase(line, obj)
	all_text__ = sv.getSentimentValue(all_text_, obj)
	sentencesentiment = sp.getSentencePolarity(all_text__)

	return sentencesentiment