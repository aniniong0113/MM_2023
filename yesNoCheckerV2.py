# functions go here
def yesNoChecker(question):
    response = input(question).lower()

    if response == "yes" or response == "y":
        print("Instructions go here")
    elif response == "no" or response == "n":
        pass
    else:
        print("please try again, please answer yes / no")


# main routine goes here
while True:

    want_instructions = yesNoChecker("Do you want to see the instructions?: ")
    if want_instructions == "yes":
        print("Instructions go here")

print("we are down")
