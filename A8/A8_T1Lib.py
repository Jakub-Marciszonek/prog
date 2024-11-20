import time

def Menu():
    print("Options:\n1 - Set pause duration\n2 - Activate pause\n0 - Exit")
    Choice = input("Your choice: ")
    if Choice.isnumeric():
        Choice = int(Choice)
    else:
        print("Unknown option!")
    return Choice

def SetPause():
    Time = float(input("Insert pause duration (s): "))
    return Time

def Pause(Time):
    print(f"Pausing for {Time} seconds.")
    time.sleep(Time)
    print("Unpaused.")