# main routine starts here

# set maximum number of tickets below

maxTickets = 3

# loop to sell tickets

ticketsSold = 0

while ticketsSold < maxTickets:
    name = input("Please enter your name or 'xxx' to quit: ")

    ticketsSold += 1

    if name == 'xxx':
        break

# output number of tickets sold

if ticketsSold == maxTickets:
    print("Congratulations you have sold all the tickets!")

else:
    print("You have sold {} ticket/s. There is {} ticket/s remaining.").format(ticketsSold, maxTickets - ticketsSold)

