import pandas as pd


def save_new_dataset(save, directory, properties) -> None:
    file = parse_file(directory, properties)
    file.to_csv(save, index=False)


def parse_file(directory, properties):
    file = pd.read_csv(directory, sep=";").fillna("nan")
    file = file.iloc[:, [0, 1, 2, file.columns.get_loc(properties)]]
    return file
