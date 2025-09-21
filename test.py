import string
ABC = string.ascii_uppercase

def configurating():
    Filename = input("Insert config(filename): ")
    try:
        with open(f"A7/{Filename}", "r") as file:  # Adjusted path
            Rotors = file.read().splitlines()
    except FileNotFoundError:
        print("File not found. Please check the filename and path.")
        return []

    for i in range(len(Rotors)):
        Pos = Rotors[i].find(":")
        Rotors[i] = Rotors[i][Pos+1:]  # Extract rotor sequence after ":"

    print("Enigma initialized")
    return Rotors

def ciphering(Rotors):
    if len(Rotors) < 4:
        print("Invalid rotor configuration.")
        return

    Rotor1, Rotor2, Rotor3, Reflector = Rotors[0], Rotors[1], Rotors[2], Rotors[3]

    No1 = No2 = No3 = 0

    while True:
        Row = ""
        INP = input("Insert row (empty stops): ").upper()

        if INP == "":
            return 
        
        for i in INP:
            if i == " ":
                Row += " "
                continue

            # Rotor 1
            Pos = (ABC.index(i) + No1) % 26
            Letter = Rotor1[Pos]

            # Rotor 2
            Pos = (ABC.index(Letter) + No2) % 26
            Letter = Rotor2[Pos]

            # Rotor 3
            Pos = (ABC.index(Letter) + No3) % 26
            Letter = Rotor3[Pos]

            # Reflector
            Pos = ABC.index(Letter)
            Letter = Reflector[Pos]

            # Backwards through Rotor 3
            Pos = Rotor3.index(Letter)
            Letter = ABC[(Pos - No3) % 26]

            # Backwards through Rotor 2
            Pos = Rotor2.index(Letter)
            Letter = ABC[(Pos - No2) % 26]

            # Backwards through Rotor 1
            Pos = Rotor1.index(Letter)
            Letter = ABC[(Pos - No1) % 26]

            print(f"Character \"{i}\" illuminated as \"{Letter}\"")
            Row += Letter

            # Step the rotors
            No1 = (No1 + 1) % 26
            if No1 == 0:
                No2 = (No2 + 1) % 26
                if No2 == 0:
                    No3 = (No3 + 1) % 26
        print(Row)
    

def main():
    print("Program starting.")
    Rotors = configurating()
    if Rotors:  # Check if configuration was successful
        ciphering(Rotors)
    print("Program ending.")

main()
