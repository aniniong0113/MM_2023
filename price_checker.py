# cash or credit function

def cash_credit(question):
    while True:
        response = input(question).lower()

        if response == "cash" or response == "ca":
            return "cash"
        elif response == "credit" or response == "cr":
            return "credit"
        else:
            print("Please choose a valid payment method such as 'cash' or 'credit'")


while True:
    payment_method = cash_credit("Which payment method would you like to use?: ")
