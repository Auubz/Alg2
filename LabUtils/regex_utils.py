import re

def is_number(a):

    return re.match("^[0-9]+$", a)

def is_special(a):

    return re.match("^[^0-9A-Za-z]$", a)

def is_even(a):
    return re.match("^\d*[02468]$", a)


        # return re.match("$\s*(\d*[0-9]\s*,\s*)*\d*[02468]$", a)


