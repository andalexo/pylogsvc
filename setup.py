"""A setuptools based setup module for the yaplog.
"""

from os.path import abspath, dirname, join
from ast import literal_eval
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

# Always prefer setuptools over distutils
from setuptools import setup, find_packages


here = abspath(dirname(__file__))

# Get the version from the __init__.py file
def get_version():
    """Scan __init__ file for __version__ and retrieve."""

    finit = join(here, 'yaplog', '__init__.py')
    with open(finit, 'r') as fd:
        for line in fd:
            if line.startswith('__version__'):
                return literal_eval(line.split('=', 1)[1].strip())
    return '0.0.0'

setup(
    name='kafka-consumer',
    version=get_version(),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={},
)
