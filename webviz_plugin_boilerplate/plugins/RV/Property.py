class Property:
	def __init__(self, name, function, file2d, folder_Dist_Matr, sortingAlgor, fileFeatVect):
		self.name = name
		self.function = function
		self.file2d = file2d
		self.fileDistMatr = folder_Dist_Matr
		self.sortingAlgor = sortingAlgor
		self.fileFeatVect = fileFeatVect
  
	def getFile2d(self):
		return (self.file2d)

	def getProperty(self):
		return (self.name+" "+self.function+" "+self.file2d)

	def convertMeanType(self):
		if self.function[0] == 'M':
			if (self.function == "MIN"):
				return 3
			elif (self.function == "MAX"):
				return 4
			elif (self.function == "MODE"):
				return 10

			elif self.function[0] == 'S':
				if (self.function == "SUM"):
					return 5
				elif (self.function == "STDEV"):
					return 6

			elif self.function[0] == 'A':
				return 7

			elif self.function[0] == 'G':
				return 8

			elif self.function[0] == 'H':
				return 9

            # else:
        # print('MeanType não esperado, favor verificar')
