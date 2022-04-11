MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
fahrenheit = eval(input('fahrenheit:'))
celsius = float(input("Celsius: "))
choice = input(">>> ").upper()
def main(choice):
    while choice != "Q":
        if choice == "C":
            Fahrenheit = covert(choice)
            print(Fahrenheit)
        elif choice == "F":
            Celsius = covert(choice)
            print(Celsius)


            # TODO: Write this section to convert F to C and display the result
         # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def covert(choice,fahrenheit,celsius):
    if choice == "C":
        fahrenheit = celsius * 9.0 / 5 + 32
        return "Result: {:.2f} F".format(fahrenheit)
    elif choice == "F":
        celsius = 5 / 9 * (fahrenheit - 32)
        return "Result: {:.2f} F".format(celsius)

main()
