import math


def birth_year(age):
    if age < 1:
        raise ValueError("Please try again!")
    return math.ceil(2018 - age)


try:
    age = int(input("How old are you ? "))
    name = input("What is your name ?  ")
    hobby = input("Do you love cycling ? ")
    if hobby == "yes":
        print("Woo! you are such a fitness freak!")
    else:
        print("you should at least ride once in a week during weekends!!")

    result = birth_year(age)

except ValueError as err:
    print("This is invalid!")
    print("({})".format(err))

else:
    friends = int(input("How many friends you have ?"))
    if friends <= 6:
        print("Wow {}! you are great!".format(name))
    else:
        print("You seems to be very popular!!")

    print("Hello {}! your birth year is {}".format(name, result))

