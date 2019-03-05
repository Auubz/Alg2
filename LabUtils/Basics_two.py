import re
Input_list = [6, "g", 5 ,"b" , "$", "c", 7, 26, 5, "z", "!"]

def regex_is_numeric(candidate):

    # x = re.search("^[0-9]+$",candidate)
    #
    # if x != None:
    #     return True
    # else:
    #     return False

    return re.match("^[0-9]+$", candidate)

i = regex_is_numeric(0)

