def Read():
    Columns = []
    Filename = input("Insert filename: ")
    with open(Filename, "r") as csvfile:
        next(csvfile)
        for Row in csvfile:
            if Row.isnumeric():
                i = int(i)
            elif Row[0].isdigit() and Row[1] == "." and Row[2].isdigit():
                Row = float(i)
            Row = Row.strip()
            if Row == "":
                continue
            Column = Row.split(";")
            Columns.append(Column)
    print(f"Reading file \"{Filename}\".\nElectricity usage:")
    return Columns

def DataProcsesing(Columns):
    for i in Columns:
        i[1] = i[1] + ":00"
        Total = float(i[2]) * float(i[3])
        i.append(Total)
    return Columns

def Display(Columns):
    for i in Columns:
        i[2] = int(i[2])
        i[3] = float(i[3])
        print(f" - {i[0]} {i[1]}, price{i[3]: .2f}, consumption\
{i[2]: .2f} kWh, total{i[4]: .2f} €")

def main():
    print("Program starting.")
    Columns = Read()
    Columns = DataProcsesing(Columns)
    Display(Columns)
    print("Program ending.")
    return None

main()