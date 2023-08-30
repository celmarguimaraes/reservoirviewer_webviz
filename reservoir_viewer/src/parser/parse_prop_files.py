import subprocess
import os
from pathlib import Path

class ParseProperties:
    def parse_file(self, save, directory, properties) -> None:
        current_file_path = Path(__file__).parent.resolve()
        executable = Path(current_file_path, "./rvweb.exe")
        save = Path(save)
        subprocess.call([executable, directory, properties, save])
