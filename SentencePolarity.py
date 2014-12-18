from Polarity import getPolarity

def getSentencePolarity(all_text):
	polar_list = [0,1]
	intensity = 0
	
	for phrase in all_text:
		phrase_att = phrase[-1]
		if phrase_att[1] == 'Positve':
			polar_list = [polar_list[0] + 1, polar_list[1] * 1]
			intensity = intensity + phrase_att[2]

		elif phrase_att[1] == 'Negative':
			polar_list = [polar_list[0] + 1,polar_list[1] * -1]
			intensity = intensity + phrase_att[2]

		else:
			polar_list = [polar_list[0] + 0,polar_list[1]]
			intensity = intensity + phrase_att[2]

	polar = getPolarity(polar_list)
	sent = []
	sent.append(all_text)
	sent.append(polar)
	sent.append(intensity)
	return sent



	
	
