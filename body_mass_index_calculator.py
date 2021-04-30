print("#########################################################\n"
      "############## Body Mass Index calculator ###############\n"
      "#########################################################\n")


# asks user to input his height
height = input("Please enter your height in m: ")

# mechanism to check if the user input is valid input
while True:

    # checks if the user input is a float
    # if it is a float it breaks the while loop and proceeds to the next block of code
    try:
        float(height)
        new_height = float(height)
        break
    # if the user input is not a float or a number, it prompts the user again for valid input
    except ValueError:
        print("Enter a valid height...")
        height = input("enter your height in m: ")
        print("")
        continue

weight = input("Please enter your weight in kg: ")

while True:
    # checks if the user input is a float
    # if it is a float it breaks the while loop and proceeds to the next block of code
    try:
        float(weight)
        new_weight = float(weight)
        break
    # if the user input is not a float or a number, it prompts the user again for valid input
    except ValueError:
        print("Enter a valid weight...")
        weight = input("enter your weight in kg:")
        print("")
        continue

# calculating the body mass index
body_mass_index = new_weight / new_height**2

# printing out the result to the user
print("\nYour BMI is " + str(round(body_mass_index, 2)))
