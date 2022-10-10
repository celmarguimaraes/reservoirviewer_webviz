class Clustering:
    def __init__(self, method, distMatrix, min, max, numIter):
        self.method = method
        self.distMatrix = distMatrix
        self.min = min
        self.max = max
        self.numIterations = numIter

    def getMethod(self): return self.method 
    def getDistMatrix(self): return self.distMatrix 
    def getMin(self): return self.min 
    def getMax(self): return self.max 
    def getNumIterations(self): return self.numIterations 
