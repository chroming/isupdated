from setuptools import setup, find_packages


setup(
    name='isupdated',
    version='0.1',
    description='Check if github repository release is updated.',
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