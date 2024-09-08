from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
name='attempts',
version='0.2',
author='Pedro Henrique Bezerra',
author_email='pedrotcp@gmail.com',
description='A very simple yet customizable package to add timestamps to your print statements.',
long_description=long_description,
long_description_content_type='text/markdown',
url='https://github.com/pedrotcp/attempts',
packages=find_packages(where="src"),
package_dir={"": "src"},
install_requires=[
"colorama>=0.4.4",  # Add colorama as a requirement
],
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)
