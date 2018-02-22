"""Excoverflow setup."""
from setuptools import setup
from excoverflow import __version__


def readme():
    """Grab the readme contents."""
    with open('README.rst') as f:
        return f.read()


desc = 'Appends google/stackoverflow search links to unhandled exceptions'


setup(
    name='excoverflow',
    version=__version__,
    description=desc,
    long_description=readme(),
    license='MIT',
    author='Christopher Flynn',
    author_email='crf204@gmail.com',
    url='https://github.com/crflynn/excoverflow',
    packages=['excoverflow'],
    zip_safe=False,
    classifiers=[
      'License :: OSI Approved :: MIT License',
      'Intended Audience :: Developers'
      'Topic :: Software Development :: Libraries :: Python Modules',
      'Programming Language :: Python',
      'Programming Language :: Python :: 2',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: Implementation :: CPython',
    ],
    include_package_data=True
)
