"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales < 1000:
    print(f'The user gets ${sales * 0.1} bonus')
    sales = float(input("Enter sales: $"))
else:
    print(f'The user gets ${sales * 0.15} bonus')
    sales = float(input("Enter sales: $"))
