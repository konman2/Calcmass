#!/usr/bin/python
import sys
import csv
import os
val = ""
try:
   val = str(sys.argv[1])
except IndexError:
   print("Enter an argument")
   sys.exit(1)

def add_commas(orig):
   with_Commas = ""
   j = -1
   for i in range(len(orig)-1):
      with_Commas += orig[i]
      if orig[i+1].isupper():
         with_Commas+=","      
   with_Commas += orig[len(orig)-1]
   return with_Commas

                  
if val.find('-'):
   val =  val.replace('-',',')
if val.find(' '):
   val = val.replace(' ',',')
if ',' not in val:
   val = add_commas(val)
      
multiples = {}
def add(mult,build):
    com = 0
    for i in range(len(build)-1,-1,-1):
        if build[i] == ',':
            com = i
            break
    if com == 0:
        symb = build[com:len(build)]
    else:
        symb = build[com+1:len(build)]
    multiples[symb] = mult

def findNum(i):
    if val[i].isalpha() or val[i] == ',':
        return val[i]
    comma = val.find(",",i)
    if comma != -1:
        num = val[i:comma]
    else:
        num = val[i:len(val)]
    return num
def run():
    lastCom = 0
    build =""
    i = 0
    while i < len(val):
        if val[i] == ',':
            lastCom = i
            build+=val[i]
        elif not val[i].isalpha():
            num = int(findNum(i))
            add(num,build)
            
        else:
            build+=val[i]
        i+=len(findNum(i))
    return build

def findRow(read,val):
   for i in read:
      if i[1].strip() == val:
         return i
   return -1
def calcSingle(val):
   count = 0
   os.chdir(os.path.dirname(os.path.abspath(__file__)))
   with open('pt-data1.csv','r') as csvfile:
      read = csv.reader(csvfile)
      row = findRow(read,val)
      if row != -1:
         num = float(row[3][:len(row[3])-3].strip())
         
         if val in multiples:
            count+=num*multiples[val]
         else:
            count+=num
      else:
         print("Not a compound")
         sys.exit(2)
   return count
            
elements = run()

def calculate():
   build = ""
   count = 0
   for i in range(len(elements)):
      if elements[i] == ",":
         count+=calcSingle(build)
         build = ""
      elif i == len(elements)-1:
         build+=elements[i]
         count+=calcSingle(build)
      else:
         build+=elements[i]
   return count

print("%0.5f" % calculate())
