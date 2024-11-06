def Inputhandling():
    List2=[]
    txt = input("Insert comma separated integers: ")
    List = txt.split(",")
    for i in List:
        if i.isnumeric() == False:
            print(f"Invalid value '{i}' detected.")
        elif i.isnumeric() == True:
            i = int(i)
            List2.append(i)
    return List2
            
def dataoperation(List2):
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
    dataoperation(Inputhandling())
    print("Program ending.")

main()