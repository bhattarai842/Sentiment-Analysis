def getPolarity(polar_list):
	if polar_list[0]>0 and polar_list[1]>0:
		return 'Positve' 
	elif polar_list[0]>0 and polar_list[1]<0:
		return 'Negative'
	else:
		return 'Undefine'
