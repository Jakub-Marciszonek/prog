import string

PlainLower = list(string.ascii_lowercase)
PlainUpper = list(string.ascii_uppercase)

def LookingFor(Data):
    print("Looking for the message in the palace...")
    # with open(f"{Data[1]}_{Data[2]}.gkg", "r") as file:
    #     Data1 = file.readlines()
    with open(f"A6/2_3.gkg", "r") as file:
        Data1 = file.readlines()
    
def Gate(Data):
    List = []
    print("Passing the guard at the entrance.")
    
    for i in Data[2]:
        if i in PlainLower:
            Character = chr((ord(i) + 13 - 97) % 26 + 97)
            List.append(Character)
        elif i in PlainUpper:
            Character = chr((ord(i) + 13 - 65) % 26 + 65)
            List.append(Character)
        else:
            List.append(i)
    Ciphered = "".join(List)
    print(Ciphered)
    
def Map(Data):
    if str(Data[0]) == "0":
        print("Currently at home")
    elif str(Data[0]) == "1":
        print("Currently at Galba's palace.")
    elif str(Data[0]) == "2":
        print("Currently at Otho's palace.")
    elif str(Data[0]) == "3":
        print("Currently at Vitellius's palace.")
    elif str(Data[0]) == "4":
        print("Currently at Vespasian's palace.")
    else:
        Data[0] = "0"
    
    if str(Data[1]) == "0":
        print("Travelling to home...")
        print("Arriving to home...")
    elif str(Data[1]) == "1":
        print("Travelling to Galba's palace...")
        print("...Arriving to the Galba's palace.")
    elif str(Data[1]) == "2":
        print("Travelling to Otho's palace...")
        print("...Arriving to the Otho's palace.")
    elif str(Data[1]) == "3":
        print("Travelling to Vitellius' palace...")
        print("...Arriving to the Vitellius' palace.")
    elif str(Data[1]) == "4":
        print("Travelling to Vespasian's palace...")
        print("...Arriving to the Vespasian's palace.")
    else:
        Data[1] = "0"
    
def main():
    print("Travel starting.")
    with open("player_progress.txt", "r") as file:
        Data0 = file.readlines()
    Data = Data0[1].split(";")

    Map(Data)
    Gate(Data)
    
    print("Travel ending.")

main()