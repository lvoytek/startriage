"""Setup.py file."""
from setuptools import setup

setup(name='startriage',
      version='0.1.0',
      description='A general Python framework for triaging systems',
      author='Lena Voytek',
      author_email='lena@voytek.dev',
      url='https://github.com/lvoytek/startriage',
      download_url='https://github.com/lvoytek/startriage/tarball/main',
      keywords=['triage', 'framework', 'middleware'],
      license='GNU General Public License v3 or later',
      classifiers=[
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU General Public License v3 or later"
          " (GPLv3+)",
          "Operating System :: POSIX :: Linux",
          "Programming Language :: Python :: 3 :: Only",
      ],
      packages=['startriage'],
      zip_safe=False)
