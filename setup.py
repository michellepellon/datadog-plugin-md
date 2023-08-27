# Standard-library dependencies
from codecs import open
from os import path

from setuptools import setup

HERE = path.dirname(path.abspath(__file__))

# Get version info
ABOUT = {}
with open(path.join(HERE, 'datadog_checks', 'md', '__about__.py')) as f:
    exec(f.read(), ABOUT)

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def parse_pyproject_array(name):
    import os
    import re


CHECKS_BASE_REQ = parse_pyproject_array('dependencies')[0]

setup(
    name='datadog-md',
    version=ABOUT['__version__'],
    description='A DataDog plugin that checks the status of Linux software RAID Multiple Device md(4) arrays',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='datadog agent md(4) check',
    url='https://github.com/michellepellon/datadog-plugin-md',
    author='Michelle Pellon',
    author_email='mgracepellon@gmail.com',
    license='BSD-3-Clause',
    classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Intended Audience :: System Administrators',
      'Topic :: System :: Monitoring',
      'License :: OSI Approved :: BSD License',
      'Programming Language :: Python :: 3.10',
    ],
    packages=['datadog_checks.md'],
)
