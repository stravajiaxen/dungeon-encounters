#!/usr/bin/env python

import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='dungeonencounters',
      version=read('VERSION'),
      description='Dungeons and Dragons 5e Encounter Simulator',
      long_description=read('README.rst'),
      long_description_content_type='text/x-rst',
      keywords='D&D encounter simulator',
      author='Matthew DeMartino',
      author_email='demartino.mcd@gmail.com',
      license='GPLv3',
      url='https://github.com/fixthisplz',  # TODO: Fix this
      download_url = 'https://github.com/fixthisplz/archive/master.zip',
      packages=find_packages(),
      package_data={
          'dungeonencounters': ['../VERSION']
      },
      install_requires=[
          
      ],
      entry_points={
          'console_scripts': [
              #'makesheets = dungeonsheets.make_sheets:main',
              #'create-character = dungeonsheets.create_character:main',
          ]
      },
      python_requires='>=3.6',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Topic :: Games/Entertainment :: Role-Playing',
      ],
)
