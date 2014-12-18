def getSentenceSentiment(all_text):
	for phrase in all_text:
		intensity = 0;		
		attr = phrase[-1]
		if att[1] == 'Positive':
			intensity=intensity + att[2]
		elif attr[1] == 'Negative':
			intensity_list = intensity - att[2]
		else:
			intensity_list = intensity + 0
	
	sent=[]	
	if intensity > 0:
		sent=['Positive' , abs(intensity)]
	elif intensity < 0:
		sent=['Negative' , abs(intensity)]
	else:
		sent=['?', abs(intensity)]

	all_text.append(sent)
	
	return all_text
