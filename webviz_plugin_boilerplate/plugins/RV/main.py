from curve import Curve
from snake_curve import SnakeCurve
from dimension import Dimension
from pixelization import Pixelization

pixelization: Pixelization = Pixelization(
    "/home/izael/Documents/git/rvweb-python/intermediary_file.csv",
    SnakeCurve(27, Dimension(6, 6)),
)
pixelization.draw()

# NOTE: Ler o arquivo para uma matriz e gerar o graph;
# As responsabilidades de código ficam melhores;
# Ler o arquivo para colocar em uma matriz, e depois colocar em outra matriz.
# Parece dois passos.
# NOTE: A partir do momento que eu for lendo, eu vou gerando o graph;
# Toda a hora você vai ter que ler o arquivo;
