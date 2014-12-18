# all_text is data_type with the list of phrase and its attribute, list of phrase is list with words in tuple and the phrase attribute is tuple in list of phrases for eg
#[[[('good','JJ',Positive)],('JP','Undefine','0.1')],[[('of','IN','Undefine')],('?','Undefine','0')]] where NP is Noun Phrase and ? mean undefine phrase

from Search import search
def getSentimentValue(all_text, obj):

	posi_words = obj.positive_list ##Collection of positive words
	neg_words = obj.negative_list#Collection of negative words
	high_words = obj.high_list##Collection of high intensity words
	moderate_words = obj.moderate_list#Collection of moderate intensity words
	low_words = obj.low_list##Collection of negative words
	
	intensity = 0
	text = []
	phrase_list = []	
	
	for phrase in all_text:
		phrase_att=phrase[-1]
		if(phrase_att[0]=='?'or phrase_att[0]=='VP'):
			phrase_att=phrase_att+(0,)
		else:
			for words in phrase[0]:
				p_opinion = search(words[0],posi_words,'Positive')
				n_opinion = search(words[0],neg_words,'Negative')
				cofficient = -1 if n_opinion == 'Negative' else 1
				if words[1] == 'JJR' or words[1]=='RBR':
					intensity = intensity + (cofficient * 0.25)
				elif words[1] == 'JJS' or words[1]=='RBS':
					intensity = intensity + (cofficient * 0.75)
				elif (words[1] == 'JJ' or words[1] == 'RB') and (n_opinion=='Negative' or p_opinion=='Positive'):
					intensity = intensity + (cofficient * 0.1)
				else:
					intensity_search = search(words[0],high_words,'TRUE')
					if intensity_search == 'TRUE':
						intensity = intensity+0.75
					else:
						intensity_search = search(words[0],moderate_words,'TRUE')
						if intensity_search == 'TRUE':
							intensity = intensity+0.25
						else:
							intensity_search = search(words[0],low_words,'TRUE')
							if intensity_search == 'TRUE':
								intensity = intensity-0.25
							else:
								intensity = intensity+0	
					
			phrase_att = phrase_att+(intensity,)
		phrase_list.append(phrase[0])
		phrase_list.append(phrase_att)
		text.append(phrase_list)
		phrase_list = []
		intensity = 0
	return text
