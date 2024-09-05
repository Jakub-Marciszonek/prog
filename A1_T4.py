Num1= int(47)
Num2= int(102)

Sum= int(Num1+Num2)
Diff= int(Num2-Num1)
Product= int(Sum*Diff)

def main():

    print(Num1, "+", Num2, "=", Sum)
    print(Num2, "-", Num1, "=", Diff)
    print(Sum, "*", Diff, "=", Product)
    print("(", Num1, "+", Num2, ") * (", Num2, "-", Num1, ") =", Product)
    return None
main()
