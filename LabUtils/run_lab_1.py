from LabUtils.regex_utils import *

list = [7, "a", "$", 6]
counter = 0
num_list = []
max_value = [0]

for x in list:

    counter += 1
    is_a_number = is_number(str(x))
    is_a_special = is_special(str(x))
    is_it_even = is_even(str(x))

    for num in num_list:
        if num > max_value:
            num = max_value



    if is_it_even:

        print("Element # " + str(counter) + " Value is a number : " + str(x) + " and is even" + str(x) + " is new greatest value")


    elif is_a_number:

        print("Element # " + str(counter) + " Value is a number: " + str(x) + " and uneven" + str(x) + "is new greatest value")



    elif is_a_special:

        print("Element # " + str(counter) + " is a special character: " + str(x))

    else:

        print("Element # " + str(counter) + " is a character: " + str(x))

