import os, sys
from glob import glob
from setuptools import setup, find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name='pyline_notify',
    version="0.0.1", 
    description="line notify api simple interface",
    long_description="",
    url='https://github.com/holly/pyline_notify',
    author='holly',
    author_email='emperor.kurt@gmail.com',
    license='MIT License',
    classifiers=[
        # https://pypi.python.org/pypi?:action=list_classifiers
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='line',
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file("requirements.txt"),
)
