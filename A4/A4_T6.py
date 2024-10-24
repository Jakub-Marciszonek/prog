print("Program starting.")

SNr = int(input("Insert a positive integer: "))
Steps = 0
List = [SNr]

while SNr != 1:
    if SNr % 2 == 0:
        SNr = SNr / 2
        List.append(int(SNr))
        Steps += 1
        continue
    else:
        SNr = (SNr * 3) + 1
        List.append(int(SNr))
        Steps += 1
        continue
print(*List, sep=" -> ")
print(f"Sequence had {Steps} total steps.")
print("\nProgram ending.")