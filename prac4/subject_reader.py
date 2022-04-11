"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data =get_data()
    print(data,end="")

    for a in data:

        print(f'{a[0]} is taught by {a[1]} and has {a[2]} students')


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    parts_1 = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        parts_1.append(parts)
    input_file.close()
    return parts_1

main()