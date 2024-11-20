from A8_T4Lib import read, Count

def menu():
    print("Options:\n1 - Calculate amount of timestamps during year\n\
2 - Calculate amount of timestamps during month\n\
3 - Calculate amount of timestamps during weekday\n0 - Exit")
    Choice = int(input("Your choice: "))
    return Choice

def main():
    print("Program starting.")
    Data = read()
    while True:
        Choice = menu()
        if Choice == 0:
            print("Exiting program.")
            break
        Count(Choice, Data)
    print("\nProgram ending.")

main()