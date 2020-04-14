from setuptools import setup
from setuptools import find_packages
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
  name = 'calcmass',
  version = '2.0',
  description = 'A script to calculate the molecular mass of a chemical compound in g/mol with its chemical formula',
  author = 'Manu Kondapaneni',
  author_email = 'manukonda11@gmail.com',
  url = 'https://github.com/konman2/Mass',
  long_description=long_description,
  long_description_content_type="text/markdown",
  download_url = 'https://github.com/konman2/Mass/archive/2.0.tar.gz',
  keywords = ['mass', 'chemical', 'compound','chemistry','element','calculator'],
  install_requires=[
        'argparse',
    ],
  packages=find_packages(),
  entry_points={
    'console_scripts': [
            'calcmass = calcmass.__main__:main'
    ],
  }
)

