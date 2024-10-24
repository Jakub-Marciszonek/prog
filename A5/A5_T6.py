def showOptions():
    print("Options:\n1 - Show count\n2 - Increase count\n\
3 - Reset count\n0 - Exit")
    return None
def askChoice():
    Feet = input("Your choice: ")
    if Feet.isnumeric() == True:
        Feet = int(Feet)
    else:
        Feet = 7
    return Feet

def main():
    Nr = 0
    print("Program starting.")
    while True:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            print(f"Current count - {Nr}\n")
        elif Choice == 2:
            Nr += 1
            print("Count increased!\n")
        elif Choice == 3:
            Nr = 0
            print("Cleared count!\n")
        elif Choice == 0:
            print("Exiting program.\n")
            break
        else:
            print("Unknown option!\n")

    print("Program ending.")
    return None
main()