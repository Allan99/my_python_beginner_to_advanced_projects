name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input(
    "You are on a dirt road,\nit has come to an end and you can go left or righ.\nWhich way would you like to go? "
).lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across."
    ).lower()

    if answer == "swim":
        print("You swam across and were eaten by an aligator.")
    elif answer == "walk":
        print(
            "You walked for many miles, ran out of water and you lost the game."
        )
    else:
        print("Not a valid option. You loose.")
elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back?"
    )

    if answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? "
        )
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You WIN!")
        elif answer == "no":
            print(
                "You ignore the stranger and they are offended and you loose."
            )
        else:
            print("Not a valid option. You loose.")

    elif answer == "back":
        print("You go back and loose.")
    else:
        print("Not a valid option. You loose.")

else:
    print("Not a valid answer. You loose.")
