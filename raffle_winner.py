# Next steps
# Add currency formatyting and headings
# Integrate this component with the base cmpoenent
# Show students that tey cA USE comments at the top
# of a component at the # end of a period so that they
# know what thgey got and what they need to do next
# add this idea to the lastdiscussion slide

# in base component remember to calculate surcharge once payment methd has been chosen

import pandas
import random


# currency formatting function
def currency(x):
    return f"${x:.2f}"


# dictionaries to hold ticker details

all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

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
print(mini_movie_frame)

print()
print('---- Raffle Winner ----')
print(f"Congratulations {winner_name}. You have won ${total_won}! YO TICKET IE FREE!")
print()
# calculate ticket and profit totals

total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency formatting
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# output table with ticket data
print(mini_movie_frame)

# output total ticket sales and profit

print(f"Total Ticket Sales: ${total:.2f}")
print(f"Total Profit: ${profit:.2f}")
