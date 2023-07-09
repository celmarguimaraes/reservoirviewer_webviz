from .IJMKey import IJMKey
from .well import Well


class WellList:
    def __init__(strategy):
        self.strategyName = strategy


def loadFile(path):
    values = []
    wellName = []
    wellType = []
    line = ""
    # Well well  // TODO CONSERTAR
    # Well *nullWell = &well // TODO
    well = None

    file = open(path, r)
    for line in file:
        values = line.split("")
        if (
            line.startswith("PRD")
            | line.startswith("INJ")
            | line.startswith("PRODUCER")
            | line.startswith("INJECTOR")
        ):
            wellName = values[1]
            wellType = values[0]

            if wellType[0] == "P":
                wellType = "PRODUCER"
                break
            elif wellType[0] == "I":
                wellType = "INJECTOR"
                break
            else:
                wellType = "UNDEFINED"
                break

            well = Well(wellName, wellType)
            well.getName()

        else:
            i = int(values[0])
            j = int(values[1])
            model = int(values[2])
            key = IJMKey("UNDEFINED", i, j, model)
            well.addCoordinates(key)
            well.getName()

    if well:
        well.updateBorders()
        self.wellList.push_back(well)
