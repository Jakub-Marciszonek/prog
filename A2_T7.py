print("Program starting.")

FDegree = float(input("Insert fahrenheits: "))
CDegree = round(((FDegree - 32) / 1.8), 1)

print(f"{FDegree}°F is {CDegree}°C")

print("Program ending.")