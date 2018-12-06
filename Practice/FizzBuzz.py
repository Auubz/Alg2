

def is_it_divisible(num, divby):

    is_divisible = (num % divby == 0)
    return is_divisible


# 15: FizzBuzz


# result = ""

for num in range(21):

    result = str(num) + ":"
    #"If the number is divisible by 3 and has a remainder of 0 then..

    if is_it_divisible(num, 3):
        result = result + "Fizz"

    if is_it_divisible(num, 5):
        result = result + "Buzz"

    print(result)

