from guitar_test import Guitar
def main():
    guitars = []
    while True:
        print("My guitars!")

        Guitar.name = input("Name:")
        Guitar.year = int(input('Year:'))
        Guitar.cost = float(input('Cost:'))
        guitars.append(Guitar(Guitar.name, Guitar.year, Guitar.cost))
        print(f'{Guitar.name}({Guitar.year}): $ {Guitar.cost:.2f} added')

        print("... snip ...")

        print('These are my guitars:')
        for i, guitar in enumerate(guitars):
            print(f"Guitar {i + 1}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{Guitar.is_vintage(guitar)}")


main()