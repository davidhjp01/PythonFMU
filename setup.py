from setuptools import setup
from setuptools.dist import Distribution
# See setup.cfg for Python package parameters

class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""
    def has_ext_modules(x):
        return True

setup(distclass=BinaryDistribution)
