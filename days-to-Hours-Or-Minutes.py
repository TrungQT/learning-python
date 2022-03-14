

def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:

        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            converted_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(converted_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("You entered a negative number, please enter a valid positive number")
    except ValueError:
        print("Your input is not a valid number. Don't break the program")


user_input = ""
while user_input != "exit":
    user_input = input("Enter a number of days and a conversion unit separated by a colon.(e.g. 45:hours)\n")
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days":days_and_unit[0], "unit":days_and_unit[1]}
    print(days_and_unit_dictionary)
    validate_and_execute()



