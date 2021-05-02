print("####################################################\n"
      "######## Welcome to the payment calculator #########\n"
      "####################################################\n")

# function to check if the user input is valid
def validate_user_input(text):
    while True:
        value = input('{}: '.format(text))
        try:
            return float(value)
        except ValueError:
            print("Invalid entry! Please check your input and try again.\n")


# asks the user for the total bill
bill = validate_user_input("What was the total bill?")

# asks the user for the tip
tip = validate_user_input("What tip would you like to give?")

# asks the user for the amount of people
total_people = validate_user_input("How many people to split the bill?")


# calculates the total bill
total_bill = bill + tip

# calculates how much everyone should pay
split_bill = total_bill / total_people

# displays the result of how much each person should pay
print("Each person should pay " + str(round(split_bill, 2)))
