import math


def split_bill(total_amount, number_of_people):
    return math.ceil(total_amount / number_of_people)


total_due = int(float(input("What is the total ?  ")))
number_of_people = int(input("How many people ?  "))

amount_due = split_bill(total_due, number_of_people)

print("each person owes ${} ".format(amount_due))

