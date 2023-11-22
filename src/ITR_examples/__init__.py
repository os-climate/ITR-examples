import sys

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError  # pragma: no cover
    from importlib.metadata import version
else:
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

import pathlib

data_dir = pathlib.Path("")
# import sysconfig
# print(sysconfig.get_paths()["purelib"])

if data_dir == pathlib.Path(""):
    data_dir = pathlib.Path(__file__).parent.parent / "data"
else:
    # Validate data_dir
    pass

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = "itr_ui"
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError
