from distutils.core import setup
setup(
  name = 'molmass',
  packages = ['molmass'],
  version = '1.0',
  description = 'A script to calculate the molecular mass of a chemical compound in g/mol with its chemical formula',
  author = 'Manu Kondapaneni',
  author_email = 'manukonda11@gmail.com',
  url = 'https://github.com/konman2/Mass',
  download_url = 'https://github.com/konman2/Mass/archive/1.0.tar.gz',
  keywords = ['mass', 'chemical', 'compound','chemistry','element','calculator'],
  data_files = [('molmass', ['mass/pt-data1.csv'])],
  entry_points = {
        "console_scripts": ['mass = molmass.mass']
  }
  classifiers = [],
)
