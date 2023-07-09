from pkg_resources import get_distribution, DistributionNotFound
from .reservoir_viewer import ReservoirViewer

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass
