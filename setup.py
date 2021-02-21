from setuptools import setup, find_packages
import sys, os

version = '0.3rc1'

setup(name='YDbf',
      version=version,
      description="Pythonic reader and writer for DBF/XBase files",
      long_description="""\
YDbf is a library for reading/writing DBF files
(also known as XBase) in a pythonic way. It
represents DBF file as a data iterator, where
each record is a dict.
""",
      classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License (GPL)',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Database',
      'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='',
      author='Yury Yurevich',
      author_email='python@y10h.com',
      url='https://github.com/y10h/ydbf',
      license='GNU GPL2',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[],
      entry_points="""
      # -*- Entry points: -*-
      [console_scripts]
      ydbfdump = ydbf.dump:main
      """,
      )
      
