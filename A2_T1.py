print("Program starting.")

Name = input("What is your name: ")
Num1 = float(input("Enter a floating point number: "))
Num2 = float(input("Enter second floating point number: "))
Equation = round((Num1 * Num2), 2)

print(Name, f"you gave numbers {Num1} and {Num2}")
print("Multiplying first and second number will result in product", Equation)
print("Program ending.")