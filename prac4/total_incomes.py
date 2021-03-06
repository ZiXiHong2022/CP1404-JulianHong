"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    incomes, number_of_months = months()

    print("\nIncome Report\n-------------")
    total = 0
    for number_of_months in range(1, number_of_months + 1):
        income = incomes[number_of_months - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(number_of_months, income, total))


def months():
    """Display income report for incomes over a given number of number_of_months."""
    incomes = []
    number_of_months = int(input("How many months? "))
    for number_of_months in range(1, number_of_months + 1):
        income = float(input("Enter income for months {} :".format(number_of_months)))
        incomes.append(income)
    return incomes, number_of_months


main()