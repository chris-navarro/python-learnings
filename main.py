
# global variables
# cal_to_units = 24
# unit_name = "hours"

# importing a function
from function import validate_and_execute, user_input_message

# initialized user_input variable
user_input = ""

# while loop with input function
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dict = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dict)
    # for num_of_days_element in set(days_and_unit):
    print(type(days_and_unit_dict))
    validate_and_execute(days_and_unit_dict)

