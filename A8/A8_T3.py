from A8_T3Lib import Readfile

def menu():
    print("Options:\n1 - Read values\n2 - Amount of values\n\
3 - Calculate sum of values\n4 - Calculate average of values\n0 - Exit")
    Choice = int(input("Your choice: "))
    return Choice

def main():
    print("Program starting.")
    while True:
        Choice = menu()
        if Choice == 1:
            List = Readfile()
            print("")
        elif Choice == 2:
            print(f"Amount of values {len(List)}\n")
        elif Choice == 3:
            print(f"Sum of values {sum(List): .1f}\n")
        elif Choice == 4:
            print(f"Average of values {sum(List)/len(List): .1f}\n")
        elif Choice == 0:
            break
    print("\nProgram ending.")

main()