import csv

def Read():
    Columns=[]
    Filename = input("Insert filename: ")
    with open(Filename, "r") as csvfile:
        next(csvfile)
        for Row in csvfile:
            Row = Row.strip()
            Column = Row.split(";")
            Columns.append(Column)
    return Columns

def DataProcsesing(Columns):
    for i in Columns:
        i[1] = i[1]+":00"
        Total = round(int(i[2])*float(i[3]), 2)
        i.append(Total)
    return Columns

def Display(Columns):
    for i in Columns:
        print(f"{i[0]} {i[1]}, price {i[3]}€, consumption {i[2]} kWh, total {i[4]}€")

def main():
    print("Program starting.")
    Columns = Read()
    Columns = DataProcsesing(Columns)
    Display(Columns)
    print("Program ending.")
main()