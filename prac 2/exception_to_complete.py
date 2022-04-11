"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    a = int
    try:
        result = int(input("Enter a valid integer: "))
        if result == a :
            result = int(input("Enter a valid integer: "))
        else:
            print('valid ')
    except ValueError:
        # TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
print("Valid result is:", result)