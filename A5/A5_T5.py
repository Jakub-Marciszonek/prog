def Menu():
    print("Options:\n1 - Insert word\n2 - Show current word\n\
3 - Show current word in reverse\n0 - Exit")
    Choice = input("Your choice: ")
    return Choice

def Storage():
    Storage = str(input("Insert word: "))
    print("")
    return Storage

def Show(Word):
    print(f"Current word - \"{Word}\"\n")

def Reverse(Word):
    print(f"Word reversed - \"{Word[::-1]}\"\n")

def main():
    Word = ""
    print("Program starting.")
    while True:
        Choice = Menu()
        if Choice == "1":
            Word = Storage()
        elif Choice == "2":
            Show(Word)
        elif Choice == "3":
            Reverse(Word)
        elif Choice == "0":
            print("Exiting program.")
            break
        else:
            print("Unknown option! try again.\n")

    print("\nProgram ending.")
    return None
main()