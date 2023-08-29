import subprocess

FILE_PATH = "../../parser"


class ParseProperties:
    def __init__(self, properties: str) -> None:
        self.properties = properties

    def parse_file(self, properties: str, directory: str) -> None:
        subprocess.run(["./rvweb", FILE_PATH, directory, properties])


if __name__ == "__main__":
    parse = ParseProperties("MAX")
    parse.parse_file("MAX", "../../parser/PERMIIGUAL800_0.0_DEFAULT_MATRIX_K.csv")
