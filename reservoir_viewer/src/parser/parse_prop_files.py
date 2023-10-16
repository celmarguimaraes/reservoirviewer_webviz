import pandas as pd
import numpy as np
import csv


class ParseProperties:
    def parse_file(self, save, directory, properties) -> None:
        file = pd.read_csv(
            directory, sep=";", usecols=["I", "J", "Model", properties]
        ).fillna("nan")

        i_max = file["I"].max()
        j_max = file["J"].max()
        model_max = file["Model"].max()
        values = str("{},{},{},{}".format(i_max, j_max, model_max, properties))

        new_record = pd.DataFrame([values])
        final = file[properties]
        final = pd.concat([new_record, final], ignore_index=True)

        final.to_csv(
            save,
            index=False,
            header=False,
            doublequote=False,
            quoting=csv.QUOTE_NONE,
            quotechar="",
            escapechar=" ",
        )
