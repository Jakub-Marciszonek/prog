print("Program starting.")

print("String comparisons")
Word = str(input("Insert first word: "))
Character = str(input("Insert a character: "))

if Character in Word:
    print(f'Word "{Word}" contains chracter "{Character}"')
else:
    print(f"Word \"{Word}\" doesn't contains chracter \"{Character}\"")

Word2 = str(input("Insert second word: "))

Words = (Word, Word2)
Order = sorted(Words)

if Word == Word2:
    print(f"Both inserted words are the same alphabetically, \"{Word}\"")
elif Order[0] == Word2:
    print(f"The second word \"{Word2}\" is before the first word \"{Word}\" alphabetically.")
else:
    print(f"The first word \"{Word}\" is before the second word \"{Word2}\" alphabetically.")

print("\nProgram ending.")