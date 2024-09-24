print("Program starting.\n")

print("Options:\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n\
0 - Exit")

Choice = int(input("Your choice: "))

if Choice == 0:
    print("Exiting...")
elif Choice == 1:
    CDegrees = float(input("Insert the amount of Celsius: "))
    print(f"{CDegrees}°C equals to {(9/5) * CDegrees + 32}°F")
elif Choice == 2:
    FDegrees = float(input("Insert the amount of Fahrenheit: "))
    print(f"{FDegrees}°F equals to 1
    {round(((FDegrees - 32) / 1.8), 1)}°C")
else:
    print("Unknown option.") 

print("\nProgram ending.")