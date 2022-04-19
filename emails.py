def main():
    email_name = {}
    email_address = input("Email: ")
    while email_address != "":
        name = get_name(email_address)
        test_name = input("Is your name {}? (Y/n) ".format(name))
        if test_name.upper() == "N" or test_name == "NO":
            name = input("Name: ")
        elif test_name.upper() == "Y" or test_name.upper() == "YES" or test_name.upper() == " ":
            pass
        else:
            name = get_name(email_address)
        email_name[email_address] = name
        email_address = input("Email: ")
    for email_address, name in email_name.items():
        print(f"{name} ({email_address})")


def get_name(email):
    find_at = email.split('@')[0]
    find_dot = find_at.split('.')
    name = " ".join(find_dot).title()
    return name


if __name__ == '__main__':
    main()