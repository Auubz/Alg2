mylist = [11,22,33,44]

for item in mylist:
    print (item)

#----------------------------------

squares = [value**2 for value in range (1,11)]
#----------------------------------

mylist2 = [value**2 for value in [11,22,33,44]]
print (mylist2)

mylist3 = [2 ** n for n in range (11)]
print (mylist3)