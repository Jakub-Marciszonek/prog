def askName():
    PName = str(input("Insert name: "))
    return PName

def greetUser(PName):
    print(f"Hello {PName}!")

def main():
    print("Program starting.")

    greetUser(askName())

    print("Program ending.")
    return None
main()