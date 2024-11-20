import string 
ABC = string.ascii_uppercase

def configurating():
    Nr = 0

    Filename = input("Insert config(filename): ")
    with open(Filename, "r") as file:
        Rotors = file.read()
    
    PlugYN = input("Insert plugs (y/n)?: ")

    Rotors = Rotors.split("\n")
    for i in Rotors:
        Pos = i.find(":")
        Rotors[Nr] = Rotors[Nr][Pos+1:]
        Nr += 1

    print("Enigma initialized")
    return Rotors

def ciphering(Rotors):
    Rotor1 = Rotors[0]
    Rotor2 = Rotors[1]
    Rotor3 = Rotors[2]
    Reflector = Rotors[3]

    while True:
        Row = ""
        No1 = No2 = No3 = 0

        INP = input("Insert row (empty stops): ").upper()

        if INP == "":
            return 
        
        for i in INP:
            if i not in ABC:
                Row += i
                continue

            # Rotor 1
            Pos = (ABC.index(i) + No1) % 26
            Letter = Rotor1[Pos]

            Pos = (ABC.index(Letter) + No2) % 26
            Letter = Rotor2[Pos]

            Pos = (ABC.index(Letter) + No3) % 26
            Letter = Rotor3[Pos]

            # Reflector
            Pos = ABC.index(Letter)
            Letter = Reflector[Pos]

            # Rotor 3 backwards
            Pos = Rotor3.index(Letter)
            Letter = ABC[(Pos - No3) % 26]

            Pos = Rotor2.index(Letter)
            Letter = ABC[(Pos - No2) % 26]

            Pos = Rotor1.index(Letter)
            Letter = ABC[(Pos - No1) % 26]

            print(f"Character \"{i}\" illuminated as \"{Letter}\"")
            Row += Letter

            No1 = (No1 + 1) % 26
            if No1 == 0:
                No2 = (No2 + 1) % 26
                if No2 == 0:
                    No3 = (No3 + 1) % 26

        print(Row)

def main():
    print("Program starting.")
    Rotors = configurating()
    ciphering(Rotors)
    print("Program ending.")
    return None
main()
