from distutils.core import setup
import os
import setuptools
import sys


if sys.version_info < (3, 6):
    raise RuntimeError("Python version is {}. Requires 3.6 or greater."
                       "".format(sys.version_info))


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        result = f.read()
    return result


setup(name='web_monitoring',
      packages=['web_monitoring'],
      scripts=['scripts/wm'],
      install_requires=read('requirements.txt').split(),
      long_description=read('README.md'),
     )
