#Find the min, max, length, sum and average of a
#list of 10 numbers
import random

#create an empty list


mylist = []

for x in mylist
    mylist.sort(0)
    for y in mylist
        









'''''
my_list = []

for x in range (20):
    for y in my_list:
        if y == x:
         continue
    else:
            my_list.append(random.randint(1,100))
            my_list.sort()
print(my_list)


max_of_list = my_list[0]
min_of_list = my_list[0]
sum_of_list = 0
length_of_list = 0

for x in my_list:
    length_of_list += 1
    sum_of_list += x

    if x > max_of_list:
        max_of_list = x

    if x < min_of_list:
        min_of_list = x


average_of_list = sum_of_list/length_of_list




print ("Sum = " + str(sum_of_list))
print ("Size = " + str(length_of_list))
print ("Largest = " + str(max_of_list))
print ("Smallest = " + str(min_of_list))
print ("Average = " +str(average_of_list))
'''