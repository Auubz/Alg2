#The reason there is 8 outputs is because (row 1 * row 2 * row 3), so (2*2*2 = 8)
for x in range(2):
    for y in range(2):
        for z in range (2):
            print (x,y,z)
            #print ("The number of times this is loops is " + str(counter))

for x in ["a","b"]:
    for y in ["c","d"]:
        for z in ["e","f"]:
            print (x,y,z)