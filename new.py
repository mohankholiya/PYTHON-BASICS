import math


def birth_year(age):
    if age < 33:
        raise ValueError("Please try again!")
    birth_year = math.ceil(2018 - age)
    return birth_year


try:
    age = int(input("How old are you?  "))
    result = birth_year(age)
except ValueError as err:
    print("Oh no! That's not a valid value...")
    print("({})".format(err))
else:
    print("birth year is {}".format(result))
