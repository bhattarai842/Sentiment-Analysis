from Search import search

def polarity(word,polar_list, posi_words, neg_words):
	p_opinion = search(str(word).strip(),posi_words,'Positive')
	n_opinion = search(str(word).strip(),neg_words,'Negative')				
	if p_opinion!='':
		polar_list=[polar_list[0]+1,polar_list[1]*1]
	elif n_opinion!='':
		polar_list=[polar_list[0]+1,polar_list[1]*-1]
	else:
		polar_list=[polar_list[0]+0,polar_list[1]*1]

	return polar_list
