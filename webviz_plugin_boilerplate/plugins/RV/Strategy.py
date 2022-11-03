class Strategy:
    def __init__(self, sSplit):
        self.name = sSplit[0]
        self.path = sSplit[1]

    def getStrategy(self):
        return (self.name+" "+self.path)