"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from ast import literal_eval

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')


def get_version(basepath):
    """Retrieve  __version__ from  __init__ file"""

    finit = basepath / 'logsvc' / '__init__.py'
    with open(finit, 'r') as fd:
        for line in fd:
            if line.startswith('__version__'):
                return literal_eval(line.split('=', 1)[1].strip())

    return '0.0.0'


setup(
    name='logsvc',
    version=get_version(here),
    description='A simple python logging module wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/andalexo/pylogsvc',
    classifiers=[
        'Intended Audience :: Developers',
    ],
    keywords='logging, development',
    packages=find_packages(),
    python_requires='>=3.6, <4',
    project_urls={
        'Source': 'https://github.com/andalexo/pylogsvc',
        'Issues': 'https://github.com/andalexo/pylogsvc/issues'
    },
    entry_points={
        'console_scripts': [
            'logsvc=logsvc.cli:main',
        ],
    },
)
