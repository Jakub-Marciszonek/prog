import datetime

MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
)
WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

def read():
    Data = []
    Filename = input("Insert filename: ")
    with open(Filename, "r") as file:
        for i in file:
            i = i.removesuffix("\n")
            Y = int(i[0:4])
            M = int(i[5:7])
            D = int(i[8:10])
            i = datetime.date(Y, M, D)
            Data.append(i)
    return Data

def Count(Choice, Data):
    Count = 0
    if Choice == 1:
        x, y = "year", "%Y"
    elif Choice == 2:
        x, y = "month", "%B"
    elif Choice == 3:
        x, y = "weekday", "%A"

    inp = input(f"Insert {x}: ")
    for i in Data:
        if i.strftime(y) == inp:
            Count += 1

    print(f"Amount of timestamps during {x} \'{inp}\' is {Count}\n")
