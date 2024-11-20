from A8_T5Lib import menu1, menu2, Reg, Log, ProfView, UserFinder, PassChange

def main():
    print("Program starting.")
    ID = -1
    while True:
        Choice = menu1()
        if Choice == "1":
            ID = Log()
            row = UserFinder(ID)
            print("")
        elif Choice == "2":
            Reg()
            print("")
        elif Choice == "0":
            print("Exiting program.\n")
            break
        while ID != -1:
            Choice = menu2()
            if Choice == "1":
                ProfView(ID, row)
                print("")
            elif Choice == "2":
                PassChange(row)
                print("")
            elif Choice == "0":
                print("Logging out...\n")
                ID = -1 

    print("Program ending.")

main()