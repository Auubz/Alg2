import os

while True:

    listing = os.listdir()

    print("-" * 50)

    for file in listing:
        print(file)

    print("-" * 50)

    a = input("Selection? >")

    if a = 