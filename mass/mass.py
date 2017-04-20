#!/usr/bin/python
from __future__ import print_function
import sys
import csv
import os

args = sys.argv
val = ""
multiples = {}
if len(args) == 1:
   print("Enter an argument")
   sys.exit(1)


def add_commas(orig):
   with_Commas = ""
   for i in range(len(orig) - 1):
      with_Commas += orig[i]
      if orig[i + 1].isupper():
         with_Commas += ","
   with_Commas += orig[len(orig) - 1]
   return with_Commas


# adds comma markers so rest of the functions can work
def add_markers(val):
   if val.find('-'):
      val = val.replace('-', ',')
   if val.find(' '):
      val = val.replace(' ', ',')
   if ',' not in val:
      val = add_commas(val)
   return val


# adds coefficients and symbol to the multiples dictionary
def add(mult, build):
   global multiples
   com = 0
   for i in range(len(build) - 1, -1, -1):
      if build[i] == ',':
         com = i
         break
   if com == 0:
      symb = build[com:len(build)]
   else:
      symb = build[com + 1:len(build)]
   multiples[symb] = mult


# returns the complete coeficcient given the starting number
def find_num(i, val):
   if val[i].isalpha() or val[i] == ',':
      return val[i]
   comma = val.find(",", i)
   if comma != -1:
      num = val[i:comma]
   else:
      num = val[i:len(val)]
   return num


# returns a string with no coefficients and builds the multiples
# dictionary
def strip_coeff(val):
   build = ""
   i = 0
   while i < len(val):
      if val[i] == ',':
         build += val[i]
      elif not val[i].isalpha():
         num = int(find_num(i, val))
         add(num, build)
      else:
         build += val[i]
      i += len(find_num(i, val))
   if len(build) == 0:
      print("Not a compound")
      sys.exit(2)
   return build


def find_row_element(read, val):
   for i in read:
      if i[1].strip() == val:
         return i
   return -1


def calc_single_element(val):
   count = 0
   os.chdir(os.path.dirname(os.path.abspath(__file__)))
   with open('pt-data1.csv', 'r') as csvfile:
      read = csv.reader(csvfile)
      row = find_row_element(read, val)
      if row != -1:
         num = float(row[3][:len(row[3]) - 3].strip())
         if val in multiples:
            count += num * multiples[val]
         else:
            count += num
      else:
         print("Not a compound")
         sys.exit(2)
   return count


def calculate(elements):
   build = ""
   count = 0
   for i in range(len(elements)):
      if elements[i] == ",":
         count += calc_single_element(build)
         build = ""
      elif i == len(elements) - 1:
         build += elements[i]
         count += calc_single_element(build)
      else:
         build += elements[i]
   return count


for i in range(1, len(args)):
   val = add_markers(args[i])
   elements = strip_coeff(val)
   if len(args) > 2:
      print(args[i] + ':', end=' ')
   print("%0.5f" % calculate(elements))
