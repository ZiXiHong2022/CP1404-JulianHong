class ProgrammingLanguage:
    def __init__(self, field, typing, reflection, year):
        self.field = field
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f" {self.field}, {self.typing} Typing, Reflection = {self.reflection} , Firstappeared in {self.year}"

    def is_dynamic(self):
        if self.typing == "Static":
            pass
        else:
            dynamic_test = True
            return dynamic_test







