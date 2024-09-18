print("Program starting.\n")

Word = str(input("Insert a closed compound word: "))
print(f"The word you inserted is '{Word}' \
and in reverse it is '{Word[::-1]}'.")
print("The inserted word length is", len(Word))
print(f"Last character is '{Word[-1]}'")

print("\nTake substring from the inserted word by inserting...")
SPoint = int(input("1) Starting point: "))
EPoint = int(input("2) Ending point: "))
SSize = int(input("3) Step size: \n"))

Substrating = Word[SPoint:EPoint:SSize]

print(f"The word '{Word}' sliced to the defined substring is \
'{Substrating}'.")

print("Program ending.")