print("Program starting.\n")

Wrds = []
Word = str()
Sum = int()
while True:
    Word = input("Insert word (empty stops): ")
    if Word == "":
        break
    Wrds.append(Word)
    Sum = Sum + len(Word)
    
print(f"\nYou inserted:\n- {len(Wrds)} words\n- {Sum} characters")
print("\nProgram ending.")