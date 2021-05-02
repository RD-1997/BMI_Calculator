print("#########################################################\n"
      "############## Body Mass Index calculator ###############\n"
      "#########################################################\n")


# function to check user input
def check_user_input(text, unit):
    while True:
        value = input("Please enter your {} in {}: ".format(text, unit))
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please check your input again.\n")

# asks user to input his height
height = check_user_input("height", "m")

weight = check_user_input("weight", "kg")

# calculating the body mass index
body_mass_index = weight / height**2

# printing out the result to the user
print("\nYour BMI is " + str(round(body_mass_index, 2)))
