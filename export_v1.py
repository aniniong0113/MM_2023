import pandas
import random
from datetime import date

# list to hold ticket rdetails

all_names = ["a", "b", "c", "d", "e"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": surcharge
}

mini_movie_frame = pandas.DataFrame(mini_movie_dict)

mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] \
                            + mini_movie_frame['Ticket Price']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

winner_name = random.choice(all_names)
win_index = all_names.index(winner_name)
total_won = mini_movie_frame.at[win_index, 'Total']


mini_movie_frame = mini_movie_frame.set_index('Name')

# get today's date
today = date.today()

# get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = f"Mini Movie Fundraiser Ticket Data ({day}/{month}/{year})\n"
filename = f"\nMMF_{year}_{month}_{day}"

# heading

print(heading)
print(f"The filename will be {filename}.txt")

mini_movie_string = pandas.DataFrame.to_string(mini_movie_frame)

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