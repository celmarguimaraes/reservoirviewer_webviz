from pkg_resources import get_distribution, DistributionNotFound
from .reservoirviewer import ReservoirViewer
from .file_parser import FileParser

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
