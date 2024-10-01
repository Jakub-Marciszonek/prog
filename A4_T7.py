print("Program starting.")

Y = 0
Number = input("Check multiplicative persistence.\nInsert an integer: ")

def ListMultiply(Smth) -> int:
    Multiply = 1
    for j in Smth:
        Multiply *= int(j)
    return Multiply

while len(str(Number)) != 1:
    X = 0
    List = []
    Number = str(Number)
    for i in Number:
        List.append(Number[X])
        X += 1

    print(*List, sep=" * ", end=" = ")
    print(ListMultiply(List))
    Number = ListMultiply(List)
    Y += 1
print(f"No more steps.\n\nThis program took {Y} step(s)")
print("\nProgram ending.")