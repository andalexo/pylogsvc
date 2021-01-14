"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from os.path import abspath, dirname, join
from ast import literal_eval

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

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
    name='yaplog',
    version=get_version(),
    description='Yet Another Python Logging module',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/andalexo/yaplog',
    classifiers=[
        'Intended Audience :: Developers',
    ],
    keywords='logging, development',
    packages=find_packages(),
    python_requires='>=3.4, <4',
    project_urls={
        'Source': 'https://github.com/andalexo/yaplog',
    },
)
