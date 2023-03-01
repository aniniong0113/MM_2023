# functions go here

# number checker

def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter an integer!!!!")

# Checks whether user has answered yes / no to a question
def yes_no_checker(question):
    response = input(question).lower()

    if response == "yes" or response == "y":
        return "yes"
    elif response == "no" or response == "n":
        return "no"
    else:
        print("please try again, please answer yes / no")

# Checks whether the name is blank
def not_blank(question):

    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. TRY AGAIN!")
        else:
            return response

# main routine goes here

# set maximum number of tickets below
max_tickets = 3

# loop to sell tickets

tickets_sold = 0

# ask user if they want to see the instructions
want_instructions = yes_no_checker("Do you want to see the instructions?: ")
if want_instructions == "yes":
    print("Instructions go here")

print()

while tickets_sold < max_tickets:
    name = not_blank("Enter your name (or 'xxx' to quit) ")

    if name == 'xxx':
        break

    age = num_check("Age: ")

    if 12 <= age <= 120:
        pass
    elif age < 12:
        print("Get outta here baby boy!!")
        continue
    else:
        print("That age does not satisfy the green m&m. Try again.")
        continue

    tickets_sold += 1

# output number of tickets sold

if tickets_sold == max_tickets:
    print("Congratulations you have sold all the tickets!")

else:
    print(f"You have sold {tickets_sold} ticket/s. There is {max_tickets - tickets_sold} ticket/s remaining.")




print("we are down")
