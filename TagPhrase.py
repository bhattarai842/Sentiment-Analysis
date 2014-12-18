from PhraseChunk import getChunkPhrase
from Search import search
import polarity
from Polarity import getPolarity

def getTagPhrase(given_text, obj):
	chunk_list = getChunkPhrase(given_text)
	tuple_append = ('#','S')
	chunk_list.append(tuple_append)
	current_value = ''
	next_value = ''
	phrase_list = []
	word_tuple = ()
	print_text = []	
	polar_list = [0,1]
	opinion = ''
	counter_first = 0
	counter_second = 0
	
	while counter_first < len(chunk_list)- 1:
		#pdb.set_trace()
		current_value = chunk_list[counter_first]
		word_tag_first = current_value[0]
		phrase_first = current_value[1]
		
		polar_list = polarity.polarity(word_tag_first[0],polar_list, obj.positive_list, obj.negative_list)##updating polariy list,polarity is the built module to find the polarity strength 
		opinion = getPolarity(polar_list)## find the polarity intensity, is built module to find the strenth of polarity
		word_tuple = (word_tag_first[0],word_tag_first[1],opinion)	
		phrase_list.append(word_tuple)			
		counter_second = counter_first + 1
		while counter_second < len(chunk_list):
			next_value = chunk_list[counter_second]
			word_tag_second = next_value[0]
			if(phrase_first == next_value[1] and phrase_first!='S'):
				polar_list = polarity.polarity(word_tag_second[0], polar_list, obj.positive_list, obj.negative_list)##module to find polarity of phrase
				##finding polarity of current token				
				opinion = ''
				opinion = search(str(word_tag_second[0]).strip(), obj.positive_list, 'Positive')
				if opinion == '':
					opinion = search(str(word_tag_second[0]).strip(), obj.negative_list, 'Negative')
					if opinion == '':
						opinion = 'Undefine'
				word_tuple = (word_tag_second[0],word_tag_second[1],opinion)	
				phrase_list.append(word_tuple)	
			else:
				counter_first = counter_second-1
				break;

			counter_second = counter_second+1
		
		counter_first = counter_first+1

		opinion = getPolarity(polar_list)
		phrase_att_list = []
		if(phrase_first == 'S'):
			add_tuple = ('?',opinion)
			phrase_att_list.append(phrase_list)
			phrase_att_list.append(add_tuple)
		else:				
			add_tuple = (phrase_first,opinion)			
			phrase_att_list.append(phrase_list)
			phrase_att_list.append(add_tuple)
		print_text.append(phrase_att_list)
		word_tuple = ()
		phrase_list = []
		polar_list = [0,1]
	return print_text



