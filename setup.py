
import io
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
DESCRIPTION = 'Check if github repository release is updated.'


try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except Exception:
    long_description = DESCRIPTION

setup(
    name='isupdated',
    version='0.1.1',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/chroming/isupdated',
    author='chroming',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',

    ],
    py_modules=["isupdated"],
    install_requires=['requests', 'six'],

)