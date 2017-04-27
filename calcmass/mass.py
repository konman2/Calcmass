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
    return with_Commas


# adds comma markers so rest of the functions can work
def add_markers(val):
    if val.find('-') != -1:
        val = val.replace('-', ',')
    if val.find(' ') != -1:
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
        symb = build[com:]
    else:
        symb = build[com + 1:]
    multiples[symb] = mult


# returns the complete coeficcient given the starting number
def find_num(i, val):
    if val[i].isalpha() or val[i] == ',':
        return val[i]
    comma = val.find(",", i)
    if comma != -1:
        num = val[i:comma]
    else:
        num = val[i:]
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
    for i in range(len(comp)):
        if comp[i] == ",":
            if build in masses:
                count += calc_single_element(build)
                build = ""
            else:
                return build
        elif i == len(comp) - 1:
            build += comp[i]
            if build in masses:
                count += calc_single_element(build)
            else:
                return build
        else:
            build += comp[i]
    return count
