import io

from setuptools import find_packages, setup
from glob import glob
from os.path import splitext, basename

setup(
    name='mwprojekt',
    version='1.0.0',
    url='https://github.com/matematyk/projekt-python',
    maintainer='Marcin Wierzbiński',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pandas',
        'pytest',
        'sklearn',
        'pytest',
        'jupyter',
        'pylint'
    ],
)