print("Program starting.")

Wrds = []
Word = str()
Sum = int()
while True:
    Word = input("Insert word (empty stops): ")
    Wrds.append(Word)
    Sum = Sum + len(Word)
    if Word == "":
        break

print(f"\nYou inserted:\n- {len(Wrds)} words\n- {Sum} characters")
print("\nProgram ending.")