print("Program starting.")

Name = str(input("This is a program with simple menu, where you can choose which operation the program performs.\n\
Before the menu, please insert your name: "))

print("\nOptions:\n1 - Print welcome message\n0 - Exit")

Choice = int(input("Your choice: "))

if Choice == 1:
    print(f"Welcome {Name}!")
elif Choice == 0:
    print("Exiting...")
else:
    print("Unknown option.")

print("\nProgram ending.")