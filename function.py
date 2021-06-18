

def days_to_units(num_of_days, unit):
    if unit == "hours":
        #define a function body
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    elif unit == "seconds":
        return f"{num_of_days} days are {num_of_days * 24 * 60 * 60} seconds"
    else:
        return f"unsupported unit"

# function2
def validate_and_execute(days_and_unit_dict):
    # if user_input.isdigit():
    try:
        days_num = int(days_and_unit_dict["days"])
        # create a conditional statement to convert positive integers
        if days_num > 0:
            cal_value = days_to_units(days_num, days_and_unit_dict["unit"])
            print(cal_value)
        elif days_num == 0:
            print("Please enter a number greater than Zero.")
        else: print("You have entered a negative number. Please enter a valid number.")

    except ValueError:
        print("Your input is either a non-integer or a float. Please enter a valid number.")

user_input_message = "Enter a number of days ':' and conversation unit:  "