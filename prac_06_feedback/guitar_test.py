class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}): worth  ${} ) ".format(self.name, self.year, self.cost)

    def get_age(self):
        age = 2022 - self.year
        return age

    def is_vintage(self):
        age_condition = Guitar.get_age(self)
        response = " (vintage)" if age_condition >= 50 else " "
        return response

