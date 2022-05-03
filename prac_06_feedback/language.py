from programming_language import ProgrammingLanguage

def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(ruby)
    print(python)
    print(visual_basic)

    #  list out when dynamically type is ture
    new_list=[ruby, python, visual_basic]
    print(" The dynamically typed language are:")
    for i in new_list:
        if ProgrammingLanguage.is_dynamic(i):
            print(i.field)
main()