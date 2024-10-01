print("Program starting.\n")

SNr = int(input("Insert starting value: "))
RNr = int(input("Insert stopping value: "))
print("\nStarting while-loop:")
while RNr >= SNr:
    if RNr == SNr:
        print(SNr)
        break
    else:
        print(SNr, end=" ")
        SNr += 1
print("\nProgram ending.")