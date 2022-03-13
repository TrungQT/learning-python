calculation_to_hours = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_hours} {name_of_unit}"


def validate_and_execute():
    try:

        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            converted_value = days_to_units(user_input_number)
            print(converted_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You entered a negative number, please enter a valid positive number")
    except ValueError:
        print("Your input is not a valid number. Don't break the program")


user_input = ""
while user_input != "exit":
    user_input = input("Enter a number of days to be converted into hours (as a comma seperated list)\n")
    print(type(user_input.split(", ")))
    print(user_input.split(","))
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()
    print(f"Please type 'exit' if you would like to close the program")



