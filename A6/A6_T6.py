import string

PlainLower = list(string.ascii_lowercase)
PlainUpper = list(string.ascii_uppercase)

def Saving(Result):
    Filename = input("Insert filename to save: ")
    Save = ("\n".join(Result))
    if Filename == "":
        print("File name not defined.")
        print("Aborting save operation.")
        return
    with open(f"{Filename}", "w") as file:
        file.write(Save)
    print("Ciphered text saved!")

def Ciphering(Words):
    print("\n#### Ciphered text ####")
    Result = []
    for Row in Words:
        List = []
        for i in Row:
            if i in PlainLower:
                Character = chr((ord(i) + 13 - 97) % 26 + 97)
                List.append(Character)
            elif i in PlainUpper:
                Character = chr((ord(i) + 13 - 65) % 26 + 65)
                List.append(Character)
            else:
                List.append(i)
        Ciphered = "".join(List)
        Result.append(Ciphered)
        print(Ciphered)
    print("\n#### Ciphered text ####")
    return Result

def Collecting():
    Words = []
    print("Collecting plain text rows for ciphering.")
    while True:
        Row = input("Insert row(empty stops): ")
        if Row == "":
            break
        else:
            Words.append(Row)
            continue
    return Words
    
def main():
    print("Program starting.\n")

    Saving(Ciphering(Collecting()))

    print("Program ending.")
    return None
main()