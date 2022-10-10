class Well:

    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.coordinates = []

def getName(self):
    print(self.name)

def addCoordinates(self, coordinates):
	self.coordinates.push_back(coordinates)


def updateBorders(self):
	for coordinate in self.coordinates:
		if (coordinate.i < self.iMin):
			self.iMin = coordinate.i
		
		if (coordinate.j < self.jMin):
			self.jMin = coordinate.j
		
		if (coordinate.i > self.iMax):
			self.iMax = coordinate.i
		
		if (coordinate.j > self.jMax):
			self.jMax = coordinate.j
		
	
