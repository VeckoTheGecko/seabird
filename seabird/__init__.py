__author__ = "Guilherme Castelao"
__email__ = "guilherme@castelao.net"

from .cnv import CNV, fCNV
from .exceptions import CNVError
import importlib.metadata

# __all__ = ['CNV', 'fCNV']

try:
    __version__ = importlib.metadata.version(__name__)
except Exception:
    try:
        from .version import version as __version__
    except ImportError:
        raise ImportError(
            "Failed to find (autogenerated) version.py. "
            "This might be because you are installing from GitHub's tarballs, "
            "use the PyPI ones."
        )
