name = input(" What is your name ? ")
age = input("What is your age ?")

print(
    "Hi {}! How are you. Wow your are just {} years old. I think this is the right time to start learning coding".format(
        name, age
    )
)

hobby = input("What are your hobbies?")

print(
    "Nice! you love {}. I too want to start {} during weekend. Can we catch up this weekend!!!".format(
        hobby, hobby
    )
)

profession = input("What are you doing ? ")

if profession == "learning python":

    print("Great! you are {}. Can you please guide me.!! ".format(profession))

elif profession == "music":
    print(
        "Wow! I love {}. I would like to compose {} one day!!  can you gudie me??".format(
            profession, profession
        )
    )

else:
    age = int(input("How old are you ? "))
    if age <= 30:
        print(
            "Wow {}. you are just {} years old. I think you should start learning coding!!".format(
                name, age
            )
        )

print("Ok {} bro. it was nice talikng to you!".format(name))

