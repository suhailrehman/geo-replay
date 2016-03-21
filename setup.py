# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='geo-replay',
    version='0.0.1',
    description='Replay web server access logs with geographically distributed servers online',
    long_description=readme,
    author='Suhail Rehman',
    author_email='suhailrehman@gmail.com',
    url='https://github.com/suhailrehman/geo-replay',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

