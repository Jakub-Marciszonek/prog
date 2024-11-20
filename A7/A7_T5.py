def Read():
    Columns = []
    Filename = input("Insert filename: ")
    with open(Filename, "r") as csvfile:
        next(csvfile)
        for Row in csvfile:
            Row = Row.strip()
            Column = Row.split(";")
            Columns.append(Column)
    print(f"Reading file \"{Filename}\".")
    return Columns

def DataProcessing(Columns):
    print("Analysing timestamps.")
    Weekdays = {"Monday": [0, 0], "Tuesday": [0, 0], "Wednesday": [0, 0], \
"Thursday":[0, 0], "Friday": [0, 0], "Saturnday": [0, 0], "Sunday": [0, 0], }
    for i in Columns:
        if i[0] in Weekdays:
            Consumption = round(float(i[2]), 2)
            Consumption = Consumption + Weekdays[i[0]][0]
            Total = round(float(i[2]) * float(i[3]), 2)
            Total = Total + Weekdays[i[0]][1]
            Weekdays[i[0]] = [round(Consumption, 2), round(Total, 2)]
    return Weekdays

def Display(Weekdays):
    print("Displaying results.")
    print("### Electricity consumption summary ###")
    for i in Weekdays:
        Usage = Weekdays[i][0]
        Cost = Weekdays[i][1]
        print(f" - {i} usage{Usage: .2f} kWh, cost{Cost: .2f} €")
    print("### Electricity consumption summary ###")

def main():
    print("Program starting.")
    Columns = Read()
    Weekdays = DataProcessing(Columns)
    Display(Weekdays)
    print("Program ending.")
    return None

main()