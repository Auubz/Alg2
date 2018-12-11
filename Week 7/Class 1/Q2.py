# QUESTION 2



def add_item(item):
    my_list.append(item)
    for x in my_list:
     print(x)
    while True:
        print(user_input)
        if item == "fin":
            break
        else:
            print(user_input)

my_list = []

user_input = input("Please Enter an element to add to the list > ")
user_input = str(user_input)

added_item = add_item(user_input)