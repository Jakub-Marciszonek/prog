import re
print("Program starting.\n")

Hex = str(input("Insert a hex color: \n"))
Pattern = r"^#[0-9A-F]{6}$"

if (re.match(Pattern, Hex)):
    print(f"Colors\n- Red {Hex[1:3]}\n- Green {Hex[3:5]}\n- Blue {Hex[5:7]}")
else:
    print("Invalid data")


print("\nProgram ending.")