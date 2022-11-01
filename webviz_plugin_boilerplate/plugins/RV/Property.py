class Property:
	def __init__(self, root, function, folder2d, folder_Dist_Matr, sortingAlgor, fileFeatVect):
		self.root = root
		self.function = function
		self.folder2d = folder2d
		self.fileDistMatr = folder_Dist_Matr
		self.sortingAlgor = sortingAlgor
		self.fileFeatVect = fileFeatVect

	def getProperty(self):
		return (self.root+" "+self.function+" "+self.folder2d)

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
