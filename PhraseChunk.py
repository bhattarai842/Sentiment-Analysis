import nltk
def getChunkPhrase(text):
	token=nltk.word_tokenize(text)
	tag_token=nltk.pos_tag(token)
	cp=nltk.RegexpParser(r"""
	  NP:{<PR.*>?<DT>?<JJ.*>*<CD>?<NN.*>+((<,>?<NN.*>?)*<CC><NN.*>)?} 
 	  VP:{<MD|TO>?<VB.*>*} 
	  JP:{<DT>?<RB.*>*<JJ.*><RB.*>*}
	  RBP:{<RB.*>+<RB.*>?}
	  """)
	output=cp.parse(tag_token)
	return output.pos()