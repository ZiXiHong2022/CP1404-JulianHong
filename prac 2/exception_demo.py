"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when enter the value are string or alphabet .
2. When will a ZeroDivisionError occur?
when enter the value of denominator is 0 .
3. Could you change the code to avoid the possibility of a ZeroDivisionError

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0 :
        print('invalid number')
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")