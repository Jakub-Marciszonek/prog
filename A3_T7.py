print("Program starting.")
print("Testing decision structures.")

Integer = int(input("Insert an integer: "))

print("Options:\n1 - In one multi-branched decision\n\
2 - In multpile independent if-statements\n0 - Exit")

Choice = int(input("Your choice: "))
while Choice != 0:
    if Choice == 1:
        if Integer >= 400:
            print(f"Using one multi-brached decision structure.\n\
Result is 272{Integer + 44}")
        elif Integer >= 200:
            print(f"Using one multi-branched decision structure.\n\
Result is {Integer + 22}")
        elif Integer >= 100:
            print(f"Using one multi-branched decision structure.\n\
Result is {Integer + 11}")
        else:
            print("Unknow option.")
    elif Choice == 2:
        if Integer >= 400:
            print(f"Using one multi-brached decision structure.\n\
Result is 272{Integer + 44+22+11}")
        elif Integer >= 200:
            print(f"Using one multi-branched decision structure.\n\
Result is {Integer + 22+11}")
        elif Integer >= 100:
            print(f"Using one multi-branched decision structure.\n\
Result is {Integer + 11}")
        else:
            print("Unknow option.")
    else:
        print("Unknow option.")            
    break
if Choice == 0:
    print("Exiting...")


print("\nProgram ending.")