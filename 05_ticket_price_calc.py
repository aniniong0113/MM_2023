# Calculate ticket price based on the age
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


while True:
    age = int(input("Age: "))
    ticket_cost = calc_ticket_price(age)
    print(f"Age: {age}, Ticket Price: ${ticket_cost:.2f}")
