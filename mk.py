first_name = input("What is your first name?  ")
print("Hello,", first_name)
if first_name == "Mohan":
    print(first_name, "is learning Python")
elif first_name == "Salman":
    print(first_name, "is learning with fellow students in the community! Me too!")
else:
    # This is just in case we have a younger user who can't yet read
    age = int(input("How old are you?  "))
    if age <= 6:
        print(
            "Wow you're {}! If you're confident with your reading already...".format(
                age
            )
        )
    print("you should totally learn python, {}!".format(first_name))
print("Have a great day {}!".format(first_name))
