print("Program starting.\n")

SNr = int(input("Insert starting point: "))
RangeNr = int(input("Insert stopping point: "))
Inspec = int(input("Insert inspection point: "))
Nrs = []
Nrs1 = []

while SNr < RangeNr and (Inspec >= SNr and Inspec <= RangeNr):
    for i in range(SNr, Inspec):
        Nrs1.append(i)
    for i in range(SNr, RangeNr):
        if i == Inspec:
            continue
        Nrs.append(i)
    print("\nFirst loop - inspection with break:")
    print(*Nrs1)
    print("Second loop - inspection with continue:")
    print(*Nrs)
    break
else:
    print("")
    while SNr >= RangeNr:
        print("Starting point value must be less than the stopping point value.")
        break
    while Inspec < SNr or Inspec > RangeNr:
        print("Inspection value must be within the range of start and stop.")    
        break

print("\nProgram ending.")
