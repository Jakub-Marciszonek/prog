print("Program starting.")

Integer1 = int(input("Insert two integers.\nInsert first integer: "))
Integer2 = int(input("Insert second integer: "))
print("Comparing inserted integers.")
if Integer1 > Integer2:
    print("First integer is greater.\n")
elif Integer2 > Integer1:
    print("Second integer is greater.\n")
else:
    print("Integers are the same.\n")

Sum = Integer1 + Integer2

print(f"Adding integers together\n\
{Integer1} + {Integer2} = {Sum}\n")

print("Checking the parity of the sum...")

OddEven = Sum % 2
if OddEven == 1:
    print("Sum is odd.")
else:
    print("Sum is even.")

print("\nProgram ending.")