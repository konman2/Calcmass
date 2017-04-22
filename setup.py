from setuptools import setup
setup(
  name = 'molmass',
  packages = ['molmass'],
  version = '0.1.1',
  description = 'A script to calculate the molecular mass of a chemical compound in g/mol with its chemical formula',
  author = 'Manu Kondapaneni',
  author_email = 'manukonda11@gmail.com',
  url = 'https://github.com/konman2/Mass',
  download_url = 'https://github.com/konman2/Mass/archive/0.1.1.tar.gz',
  keywords = ['mass', 'chemical', 'compound','chemistry','element','calculator'],
  include_package_data = True,
    package_data = {'molmass' : ['data/*.csv']},
  entry_points={
    'console_scripts': [
            'molmass = molmass.__main__:main'
    ],
  }
)
