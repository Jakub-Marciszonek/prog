print("Program starting.")

SNr = int(input("Insert starting value: "))
RangeNr = int(input("Insert stopping value: "))
Inspec = int(input("Insert inspection point: "))
Nrs = []
Nrs1 = []

if SNr >= RangeNr:
    print("Starting point value must be less than the stopping point value.")
elif Inspec < SNr or Inspec > RangeNr:
    print("Inspection value must be within the range of start and stop.")    
else:
    for i in range(SNr, Inspec):
        Nrs1.append(i)
    for i in range(SNr, RangeNr):
        Nrs.append(i)
    
    print("\nFirst loop - inspection with break:")
    print(*Nrs1)
    print("Second loop - inspection with continue:")
    print(*Nrs)


print("\nProgram ending.")