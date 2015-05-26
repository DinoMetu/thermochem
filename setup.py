from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
import thermopy

setup(name="thermopy",
      version=thermopy.__version__,
      description="Some utilities for Thermodynamics and Thermochemistry",
      author="Adel Qalieh",
      author_email="adelq@sas.upenn.edu",
      url="https://github.com/adelq/thermopy",
      license="BSD",
      packages=find_packages(),
      include_package_data=True,
      install_requires=['scipy>=0.6.0', 'numpy>=1.2.1'],
      zip_safe=False,
      keywords='thermo chemistry physics',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.5',
          'Topic :: Scientific/Engineering :: Chemistry',
          'Topic :: Scientific/Engineering :: Physics',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
      )
