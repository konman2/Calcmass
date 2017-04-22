from __future__ import print_function
from calcmass import mass
import sys

def main():
   args = sys.argv
   if len(args) == 1:
      print("Enter an argument")
      sys.exit(1)
   for i in range(1, len(args)):
      val = mass.add_markers(args[i])
      elements = mass.strip_coeff(val)
      if len(args) > 2:
         print(args[i] + ':', end=' ')
      print("%0.5f" % mass.calculate(elements))


if __name__ == "__main__":
   main()
