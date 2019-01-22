# for num in range(1, 21):
#     print(str(num) + ":", end="")
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print()


#This is not the preffered method but it works






def is_divisible(num,test_num):
    if num % test_num == 0:
        return True
    return False

for num in range(1,21):
    print(str(num) + ":", end="")
    if is_divisible(num, 3) and is_divisible(num, 5):
        print("FizzBuzz")
    elif is_divisible(num, 3):
        print ("Fizz")
    elif is_divisible(num,5):
        print("Buzz")
    else:
        print()


#HOMEWORK = Chapter 8: Functions



# def fizz_buzz(n):
#
#     alg1= (if n % 3 == 0)
#     alg2= (if n % 5 == 0)
#     alg3= (if n % 3 == and n % 5 == 0)
#
# print(str(num) + ":", end="")
#
#