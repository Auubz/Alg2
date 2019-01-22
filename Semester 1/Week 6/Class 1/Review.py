# 8.5 ----------------------------
def describe_city(city, country):
    print("The city of " + city.title() + "is located in " + country.title())


describe_city("montreal", "canada")


#8.6 -----------------------------


def city_country(city, country):
    print (str(city) + "," + str(country))

city_country( "\"Montreal "," Canada\"")


#8.9 ------------------------------
my_list = ["Bob", "Jim", "Rick", "Alfred"]

def show_magicians(magician_list):
    for magician in my_list:
        print (magician)

show_magicians(my_list)