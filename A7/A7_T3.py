import csv

def ReadFile():
    Rows = []
    Filename = input("Insert filename: ")
    with open(Filename, "r") as csvfile:
        next(csvfile)
        for line in csvfile:
            line = line.strip()
            if line:
                Rows.append(line)

    print(f"Analysing file \"{Filename}\"")
    return Rows

def Analyse(Rows):
    Weekday_counts = {"Monday":0 , "Tuesday":0 , "Wednesday":0, \
"Thursday":0, "Friday":0, "Saturnday":0, "Sunday":0,}
    for row in Rows:
        columns = row.split(";")
        Weekday = columns[0]
        if Weekday in Weekday_counts:
            Weekday_counts[Weekday] += 1
        else:
            Weekday_counts[Weekday] = 1
    Results = list(Weekday_counts.items())
    return Results

def Display(Results):
    print("Rows per Weekday:")
    for Weekday, count in Results:
        print(f"{Weekday}:{count}")

def main():
    print("Program starting.")
    Data = ReadFile()
    Result = Analyse(Data)
    Display(Result)
    print("Program ending.")

main()