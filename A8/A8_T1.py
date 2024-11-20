from A8_T1Lib import Menu, SetPause, Pause

def main():
    print("Program starting.")
    Time = -1
    while True:
        Choice = Menu()
        if Choice == 1:
            Time = SetPause()
        elif Choice == 2:
            if Time == -1:
                print("Pause is not set.\nSet pause first.")
            else:
                Pause(Time)
        elif Choice == 0:
            print("Exiting program.\n")
            break
        print("")
    print("Program ending.")
    return None
main()