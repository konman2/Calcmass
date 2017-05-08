from setuptools import setup
setup(
  name = 'calcmass',
  packages = ['calcmass'],
  version = '1.5',
  description = 'A script to calculate the molecular mass of a chemical compound in g/mol with its chemical formula',
  author = 'Manu Kondapaneni',
  author_email = 'manukonda11@gmail.com',
  url = 'https://github.com/konman2/Mass',
  download_url = 'https://github.com/konman2/Mass/archive/1.5.tar.gz',
  keywords = ['mass', 'chemical', 'compound','chemistry','element','calculator'],
  entry_points={
    'console_scripts': [
            'calcmass = calcmass.__main__:main'
    ],
  }
)
