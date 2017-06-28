# Mass
A python script to find the molecular mass in g/mol of a chemical equation
## Example
```
$ calcmass C6H12O6
180.15588
$ calcmass Cr2O7
215.98800
$ calcmass C11H22
154.29238
$ calcmass Al2Si2O5[OH]4
258.16044
```
## Setup
You can download using PyPi

Using pip:
```
$ pip install --user calcmass
```
For system wide download(Not Suggested):
```
$ sudo pip install calcmass
```
Or download the zip file at https://pypi.python.org/pypi/calcmass/1.5

Then run:
```
$ python setup.py install
```
If the calcmass command is not found add this to your .bashrc or .bash_profile

MacOs:
```
export PATH=$PATH:$HOME/Library/Python/2.7/bin
```
Linux:
```
export PATH=$PATH:$HOME/.local/bin
```

## License
Mass is licensed under the MIT License - see the LICENSE file for details.
