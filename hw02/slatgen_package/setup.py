#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Andrew Petrukhin",
    author_email='dartmol2300@gmail.com',
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.10',
    ],
    description="Simplified LaTeX Generator",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='slatgen',
    name='slatgen',
    packages=find_packages(include=["slatgen"]),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/petrukhinandrew/slatgen',
    version='0.2.0',
    zip_safe=False,
)
