#!/usr/bin/env python

from setuptools import setup

the_scripts = ['scripts/generate_frequencies','scripts/generate_samples',
               'scripts/run_fast']

setup(name='pyfast',
       version='0.1.2',
       license='GPL v3',
       description='Utility functions for Sensitivity Analysis.',
       author='David Coss',
       author_email='David.Coss@stjude.org',
       packages=['pyfast'],
       scripts=the_scripts,
       )
