list1 = ["champlain","dawson", "vanier"]

for schools in  list1:
    print (schools.upper())

list = []
#=======================================
for x in range (1,11):
    power = x**2
    list.append(power)
print(list)
#This code can also be simplified into:
for x in range (1,11):
    list.append(x**2)
print(list)

var1 = [x**2 for x in range (1,11)]
#This is read: x is taken to the power of two for all of the variables in the range 1 to 11
print(var1)

#=======================================
numbers = [1,2,3,4,5,6,7,8,9]

print(min(numbers))
max(numbers)
sum(numbers)
#==================================

for s in range (1,20,2):
    print (s)

for s in range(3,30,3):
    print (s)

var1 = [x**3 for x in range(1,11)]
print(var1)

def book(pet_name,type="dog"):
    print("I have a " + pet_name + " his name is " + type)


book("fuck you")

#===========================================
def make_shirt(text,size = "large"):
    print("The shirt will print " + text + " in size " + size)

make_shirt(str(12),"Fuck You")
make_shirt(text="haha")

#==================================================

def pet(pm, at=dog):

    pet(at=cat)

#=================================================

