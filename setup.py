#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='Mbojereha',
      version='0.9',
      description='Traducción castellano-guaraní',
      author='Michael Gasser',
      author_email='gasser@indiana.edu',
      url='http://homes.soic.indiana.edu/gasser/plogs.html',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Information Technology',
          'Natural Language :: Spanish',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Programming Language :: Python :: 3',
          'Topic :: Text Processing'
      ],
      install_requires=["python-docx"],
      python_requires='>=3',
      packages=find_packages(where="src"),
      package_dir={'': "src"},
      package_data = {'mbojereha':
                      ['languages/grn/*', 'languages/grn/fst/*.pkl',
                       'languages/grn/lex/*', 'languages/grn/syn/*',
                       'languages/grn/stat/*', 'languages/grn/grp/*',
                       'languages/spa/*', 'languages/spa/fst/*.pkl',
                       'languages/spa/lex/*', 'languages/spa/syn/*',
                       'languages/spa/stat/*', 'languages/spa/grp/*'
#                       'morphology/*'
                       ]}
     )
