print("Program starting.")
print("This is a program with simple menu, where you can choose which operation the program performs.")

Name = str(input("Before the menu, please insert your name: "))
print("\nOptions:\n1 - Print welcome message\n2 - Print the name backwards\n\
3 - Print the first character\n4 - Show the amount of characters in the name\n\
0 - Exit")

Choice = int(input("Your choice: "))

if Choice == 0:
    print("Exiting...")
elif Choice == 1:
    print(f"Welcome {Name}!")
elif Choice == 2:
    print(f"Your name backwards is \"{Name[::-1]}\"")
elif Choice == 3:
    print(f"The first character in name \"{Name}\" is \"{Name[0]}\"")
elif Choice == 4:
    print(f"There are {len(Name)} characters in the name \"{Name}\"")
else:
    print("Unknown option.")

print("\nProgram ending.")