class Property:
    def __init__(self, file2d, sorting_algor):
        self.file2d = file2d
        self.sorting_algor = sorting_algor

    def getFile2d(self):
        return self.file2d

    def getProperty(self):
        return self.name + " " + self.function + " " + self.file2d

    def convertMeanType(self):
        if self.function[0] == "M":
            if self.function == "MIN":
                return 3
            elif self.function == "MAX":
                return 4
            elif self.function == "MODE":
                return 10

            elif self.function[0] == "S":
                if self.function == "SUM":
                    return 5
                elif self.function == "STDEV":
                    return 6

            elif self.function[0] == "A":
                return 7

            elif self.function[0] == "G":
                return 8

            elif self.function[0] == "H":
                return 9

                # else:
                # print('MeanType não esperado, favor verificar')
