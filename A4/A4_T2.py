print("Program starting.\n")

SNr = int(input("Insert starting value: "))
RangeNr = int(input("Insert stopping value: "))
Nrs = []

print("\nStarting for-loop:")
for i in range(SNr, (RangeNr + 1)):
    Nrs.append(i)
print(*Nrs, sep=" ")

print("\nProgram ending.")