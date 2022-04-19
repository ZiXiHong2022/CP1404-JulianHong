CODE_TO_NAME = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                "Alizarin crimson": "#e32636",
                "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7",
                "Aqua": "#00ffff", "Aquamarine1": "#7fffd4", "Army Green": "#4b5320"}
print(CODE_TO_NAME)

name_color = input(str("Enter color name: ")).upper()
while name_color != "":
    if name_color in CODE_TO_NAME:
        print(name_color, "is", CODE_TO_NAME[name_color])
    else:
        print("Invalid color name")
        state_code = input("Enter color name: ")
