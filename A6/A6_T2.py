def main():
    print("Program starting.")
    Name = input("Insert first name: ")
    LName = input("Insert last name: ")
    File = input("Insert filename: ")
    Data = (f"{Name}\n{LName}\n")
    with open(f"{File}", "w") as file:
        file.write(Data)
    print("Program ending.")
    return None
main()