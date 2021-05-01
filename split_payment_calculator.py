print("####################################################\n"
      "######## Welcome to the payment calculator #########\n"
      "####################################################\n")

# asks the user for the total bill
bill = input("What was the total bill? ")

# mechanism to check if the user input is valid input
while True:
    try:
        # checks if the user input is a float
        # if it is a float it breaks the while loop and proceeds to the next block of code
        float(bill)
        float_bill = float(bill)
        break
    except ValueError:
        # if the user input is not a float or a number, it prompts the user again for valid input
        print("\nEnter a valid number...")
        bill = input("What was the total bill? ")
        print("")
        continue

# asks the user for the tip
tip = input("How much tip would you like to give? ")

# mechanism to check if the user input is valid input
while True:
    try:
        # checks if the user input is a float
        # if it is a float it breaks the while loop and proceeds to the next block of code
        float(tip)
        float_tip = float(tip)
        break
        # if the user input is not a float or a number, it prompts the user again for valid input
    except ValueError:
        print("\nEnter a valid number...")
        tip = input("How much tip would you like to give? ")
        print("")
        continue

# asks the user for the amount of people
total_people = input("How many people to split the bill? ")

# mechanism to check if the user input is valid input
while True:
    try:
        # checks if the user input is an integer
        # if it is an integer it breaks the while loop and proceeds to the next block of code
        int(total_people)
        int_total_people = int(total_people)
        break
        # if the user input is not a float or a number, it prompts the user again for valid input
    except ValueError:
        print("\nEnter a valid number...")
        total_people = input("How many people to split the bill?? ")
        print("")
        continue

# calculates the total bill
total_bill = float_bill + float_tip

# calculates how much everyone should pay
split_bill = total_bill / int_total_people

# displays the result of how much each person should pay
print("\nEach person should pay " + str(round(split_bill, 2)))
