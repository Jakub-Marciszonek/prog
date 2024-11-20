from A8_T2Lib import add, substract, mutiply, divide

def askValue(PPrompt):
    Value = input(PPrompt + ": ")
    return Value

def askChoice():
    Choice = int(input("Your choice: "))
    return Choice

def showOptions():
    print("Options:\n1 - Add\n2 - Substract\n3 - Multiply\n\
4 - Divide\n0 - Exit")
    return None

def main():
    print("Program starting.")
    while True:
        showOptions()
        Choice = askChoice()
        if Choice == 1:
            Val1 = float(askValue("Insert first addend value"))
            Val2 = float(askValue("Insert second addend value"))
            Sum = add(Val1, Val2)
            print(f"{Val1} + {Val2} = {Sum}")
        elif Choice == 2:
            Val1 = float(askValue("Insert minued value"))
            Val2 = float(askValue("Insert subtranhend value"))
            Sub = substract(Val1, Val2)
            print(f"{Val1} - {Val2} = {Sub}")
        elif Choice == 3:
            Val1 = float(askValue("Insert multiplicand value"))
            Val2 = float(askValue("Insert multiplier value"))
            Sum = mutiply(Val1, Val2)
            print(f"{Val1} * {Val2} = {Sum}")
        elif Choice == 4:
            Val1 = float(askValue("Insert dividend value"))
            Val2 = float(askValue("Insert divisor value"))
            Sum = divide(Val1, Val2)
            print(f"{Val1} / {Val2} = {Sum}")
        elif Choice == 0:
            print("Exiting program.\n")
            break
        print("")
    print("Program ending.")
    return None
main()