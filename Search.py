import re
def search(word,collection,opinion):
	word = re.sub(r'[^\w\s]','',word)
	if word in collection:
		return opinion
	else:
		return ''