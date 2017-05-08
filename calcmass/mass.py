#!/usr/bin/python
from __future__ import print_function
from pt_data import masses
val = ""
multiples = {}


def add_commas(orig):
    with_Commas = ""
    for i in range(len(orig) - 1):
        with_Commas += orig[i]
        if orig[i + 1].isupper():
            with_Commas += ","
    with_Commas += orig[-1]
    with_Commas += ','
    return with_Commas


# returns the complete coeficcient given the starting number
def find_num(i, val):
    if val[i].isalpha() or val[i] == ',':
        return val[i]
    count = i
    while(count < len(val) and not val[count].isalpha() and val[count] != ","):
        count += 1
    if count >= len(val):
        return val[i:]
    return val[i:count]


# distributes the vnumber to all the numbers in the string
def distribute(val, num):
    build = ""
    sub = 1
    for i in range(len(val)):
        if not val[i].isalpha():
            sub = int(find_num(i, val))
            sub *= num
            build += str(sub)
            i += len(find_num(i, val)) - 1
        elif i+1 >= len(val) or (val[i+1].isupper()):
            sub = 1*num
            build += val[i]
            build += str(sub)
            i += len(find_num(i, val))
            sub = 1
        else:
            build += val[i]
    return build

# distributes the number through parenthesis
def distrib_parenth(val):
    between = ""
    op = val.find('(')
    num = 1
    while(op != -1):
        close = val.find(')', op)
        between = val[op+1:close]
        if close+1 < len(val) and not val[close+1].isalpha() and val[close+1] != '':
            num = int(val[close+1])
            val = val[:op] + distribute(between, num) + val[close+2:]
        else:
            val = val[:op] + distribute(between, num) + val[close+1:]
        op = val.find('(', op+1)
        num = 1
    return val


# adds comma and parenthesis markers so rest of the functions can work
def add_markers(val):
    if "[" in val and "]" in val:
        val = val.replace("[","(")
        val = val.replace("]",")")
        val = distrib_parenth(val)
    if ',' not in val:
        val = add_commas(val)
    return val


# adds coefficients and symbol to the multiples dictionary
def add(mult, symb):
    global multiples
    com = symb.find(",")
    if com >= 0:
        symb = symb[:com]
    if symb not in multiples:
        multiples[symb] = mult
    else:
        multiples[symb] += mult


# returns a string with no coefficients and builds the multiples
# dictionary
def strip_coeff(val):
    build = ""
    symb = ""
    coeff = False
    i = 0
    while i < len(val):
        if not val[i].isalpha() and val[i] != ',':
            num = int(find_num(i, val))
            add(num, symb)
            coeff = True
        if val[i] == ',':
            if val[i].isalpha() or val[i] == ',':
                symb += val[i]
            if not coeff:
                add(1,symb)
            build += symb
            symb = ""
            coeff = False
        elif val[i].isalpha():
            symb += val[i]
        i += len(find_num(i, val))
    if len(build) == 0:
        return ""
    return build


def calc_single_element(val):
    count = 0
    num = float(masses[val][:len(masses[val]) - 3].strip())
    if val in multiples:
        count += num * multiples[val]
    else:
        count += num
    return count


# returns a mass if all elements are real
# otherwise returns the name of the offending element
def calculate(comp):
    build = ""
    count = 0
    finished = []
    for i in range(len(comp)):
        if comp[i] == ",":
            if build in masses and build not in finished:
                count += calc_single_element(build)
                finished.append(build)
            elif build not in masses:
                return build
            build = ""
        elif i == len(comp) - 1:
            build += comp[i]
            if build in masses and build not in finished:
                count += calc_single_element(build)
                finished.append(build)
            elif build not in masses:
                return build
        else:
            build += comp[i]
    return count
