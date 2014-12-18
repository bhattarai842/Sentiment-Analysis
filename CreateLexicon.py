class CreateLexicon:
	positive_list = []
	neagative_list = []
	moderate_list = []
	high_list = []
	low_list = []

	
	def __init__(self, dirname = './data/'):
		positive_list_path = dirname + '/positive'
		negative_list_path = dirname + '/negative'
		moderate_list_path = dirname + '/moderate' 
		low_list_path = dirname + '/low' 
		high_list_path = dirname + '/high'

		def read_file(path):
			fread = open(path,'r').read().split('\n')
			return fread

		self.positive_list = read_file(positive_list_path)
		self.negative_list = read_file(negative_list_path)
		self.high_list = read_file(high_list_path)
		self.low_list = read_file(low_list_path)
		self.moderate_list = read_file(moderate_list_path)
	
	
	
		

