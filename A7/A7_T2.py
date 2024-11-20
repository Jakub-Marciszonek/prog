import string

ABC = string.ascii_letters

def Inputhandling():
    List2 = []
    txt = input("Insert comma separated integers: ")
    List = txt.split(",")
    for i in List:
        if i == "":
            continue
        if i.isnumeric() == False:
            print(f"Invalid value '{i}' detected.")
            continue
        else:
            i = int(i)
            List2.append(i)
    return List2

def dataoperation(List2):
    if List2 == []:
        print("No values to analyse.")
        return
    EvenOdd = ""
    Sum = sum(List2)
    if Sum % 2 == 0:
        EvenOdd = "even"
    else:
        EvenOdd = "odd"

    print(f"There are {len(List2)} integers in the list.")
    print(f"Sum of the integers is {Sum} and it's {EvenOdd}")

def main():
    print("Program starting.")
    Data = Inputhandling()
    dataoperation(Data)
    print("Program ending.")
    return None

main()