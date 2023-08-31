import pandas as pd

class ParseProperties:
    def parse_file(self, save, directory, properties) -> None:
        file = pd.read_csv(directory, sep=";", usecols=[properties])
        file.to_csv(save)
