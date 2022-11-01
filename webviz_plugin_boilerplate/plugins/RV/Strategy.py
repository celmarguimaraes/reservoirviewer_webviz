class Strategy:
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def getStrategy(self):
        return (self.name+" "+self.path)