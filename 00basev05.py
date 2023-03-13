import pandas
import random
from datetime import date

# functions go here

# ticket price calculator
def calc_ticket_price(var_age):
    ticket_price = 1
    if 12 <= var_age <= 15:
        ticket_price = 7.50
        return ticket_price
    elif 16 <= var_age <= 64:
        ticket_price = 10.50
        return ticket_price
    else:
        ticket_price = 6.50
        return ticket_price


# number checker

def num_check(question):
    while True:

        try:
            response = int(input(question))
            return response
        except ValueError:
            print("Please enter an integer!!!!")


# Checks whether user has answered string to
def string_checker(question, num_letters, valid_responses):
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"

    if num_letters == 1:
        short_version = 1
    else:
        short_version = 2

    while True:

        response = input(question).lower()

        for item in valid_responses:
            if item[:short_version] == response or response == item:
                return item

        print(error)


# Checks whether the name is blank
def not_blank(question):
    while True:
        response = input(question)

        if response == "":
            print("Sorry this can't be blank. TRY AGAIN!")
        else:
            return response


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# main routine goes here

# set maximum number of tickets below
max_tickets = 30

# loop to sell tickets

tickets_sold = 0

# lists for string checker
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Lists  to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharges
}

# ask user if they want to see the instructions
want_instructions = string_checker("Do you want to see the instructions?: ", 1, yes_no_list)
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

    ticket_cost = calc_ticket_price(age)

    pay_method = string_checker("Choose a payment method (cash / credit): ",
                                2, payment_list)

    if pay_method == "credit":
        surcharge = .05 * ticket_cost
    else:
        surcharge = 0

    # add ticket details to lists...
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharges.append(surcharge)

    tickets_sold += 1

# output number of tickets sold
if tickets_sold == max_tickets:
    print("Congratulations you have sold all the tickets!")

else:
    print()
    print(f"You have sold {tickets_sold} ticket/s. There is {max_tickets - tickets_sold} ticket/s remaining.")
    print()
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
# mini_movie_frame = mini_movie_frame.set_index('Name')

mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame["Ticket Price"]
# calculate the profit for each ticket

mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# choose a winner from our name list
winner_name = random.choice(all_names)

# get position of winner name in list
win_index = all_names.index(winner_name)

# look up total amount won (ie: ticket price + surchage)
total_won = mini_movie_frame.at[win_index, 'Total']

# set index at end (before printing)
mini_movie_frame = mini_movie_frame.set_index('Name')

# get date
today = date.today()

# get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# get heading and filename
heading = f"Mini Movie Fundraiser Ticket Data ({day}/{month}/{year})\n"
filename = f"\nMMF_{year}_{month}_{day}"

# heading

print(heading)
print(f"The filename will be {filename}.txt")

print()
print(mini_movie_frame)

print()
print('---- Raffle Winner ----')
print(f"Congratulations {winner_name}. You have won ${total_won}! YO TICKET IE FREE!")
print()

# calculate ticket and profit totals

total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

ticket_cost_heading = "\n---- Ticke Cost / Porfit ----"
total_ticket_sales = f"Total Ticke Sales: ${total}"
total_profit = f"Total Profit : ${profit}"

sales_status = "\n*** All the tickets have been sold ***"

winner_heading = "\n---- Raffle Winner ----"
winner_text = f"The Winner of the raffle is {winner_name}" \
                f"They have won ${total_won}. ie: Their ticket is free!"
to_write = [heading, mini_movie_string, ticket_cost_heading,
            total_ticket_sales, total_profit, sales_status,
            winner_heading, winner_text]
for item in to_write:
    print(item)

write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

text_file.close()

# Currency formatting
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# output table with ticket data
print()
print(mini_movie_frame)

# output total ticket sales and profit

print()
print(f"Total Ticket Sales: ${total:.2f}")
print(f"Total Profit: ${profit:.2f}")
print()

print("we are down")
