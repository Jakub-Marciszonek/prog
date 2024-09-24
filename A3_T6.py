print("Program starting.")
print("Welcome to the unit converter program!\n\
Follow the menu instructions below.\n")

print("Options:\n1 - Length\n2 - Weight\n0 - Exit")

Choice = int(input("Your choice: "))
while Choice != 0:
    if Choice == 1:

        print("\nLength options:\n1 - Meters to kilometers\n\
2 - Kilometers to meters\n0 - Exit")
        Choice = int(input("Your choice: "))
        if Choice == 1:
            Meters = float(input("Insert meters: "))
            print(f"{round(Meters, 1)} m is {round((Meters / 1000), 1)} km")
            break
        elif Choice == 2:
            Km = float(input("Insert kilometers: "))
            print(f"{Km} km is {round((Km * 1000), 1)} m")
            break
        else:
            print("Unknown option.")
            break
    elif Choice == 2:

        print("\nWeight options:\n1 - Grams to pounds\n2 - Pounds to grams\n0 - Exit")
        Choice = int(input("Your choice: "))
        if Choice == 1:
            Grams = float(input("Insert grams: "))
            print(f"{Grams} g is {round((Grams/453.6), 4)} lb")
            break
        elif Choice == 2:
            Pounds = float(input("Insert pounds: "))
            print(f"{round(Pounds, 1)} lb is {round((453.59 * Pounds), 1)} g")
            break
        else:
            print("Unknown option.")
            break
    else:

        print("Unknown option.")
        break

if Choice == 0:
    print("Ending...")

print("\nProgram ending.")
