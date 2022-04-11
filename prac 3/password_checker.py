"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""
def main():
    MIN_LENGTH = 2
    MAX_LENGTH = 6
    SPECIAL_CHARS_REQUIRED = False
    SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),password))
    print("the password length is {}",format(len(password) * "*"))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < MIN_LENGTH and len(password) > MAX_LENGTH :
        return False
    else:
        count_lower = 0
        count_upper = 0
        count_digit = 0
        count_special = 0
        for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
            if str(char) == char.islower():
                count_lower += 1
            elif str(char) == char.isupper():
                count_upper += 1
            elif str(char) == char.isdigit():
                count_digit += 1
            pass

    # TODO: if any of the 'normal' counts are zero, return False
        list_1 = [count_lower,count_upper ,count_digit ,count_special]
        for i in list_1:
            if i == 0:
                return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero
        for count_special in password:
            if count_special in SPECIAL_CHARACTERS:
                count_special += 1
        if count_special == 0:
            return False
    # if we get here (without returning False), then the password must be valid

        return True


main()