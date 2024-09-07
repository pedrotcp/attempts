from setuptools import setup, find_packages

setup(
name='attempts',
version='0.1',
author='Pedro Henrique Bezerra',
author_email='pedrotcp@gmail.com',
description='A very simple yet customizable package to add timestamps to your print statements.',
long_description='A very simple yet customizable package to add timestamps to your print statements. You can replace the default print(), keeping all of its default options, or use the built-in printt() command, which accepts all the same arguments.',
long_description_content_type='text/markdown',
url='https://github.com/pedrotcp/attempts',
packages=find_packages(where="src"),
package_dir={"": "src"},
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)