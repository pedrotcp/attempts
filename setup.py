from setuptools import setup, find_packages

setup(
name='attempts',
version='0.1.0',
author='Pedro Henrique Bezerra',
author_email='pedrotcp@gmail.com',
description='A very simple yet customizable package to add timestamps to your print statements.',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)