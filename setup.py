import io

from setuptools import find_packages, setup

setup(
    name='projekt',
    version='1.0.0',
    url='https://github.com/matematyk/projekt-python',
    maintainer='Marcin Wierzbiński',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pandas',
        'pytest',
        'sklearn',
        'pytest'
    ],
)