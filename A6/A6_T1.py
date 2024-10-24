def main():
    print("Program starting.")
    File = input("This program can read a file.\nInsert filename: ")
    with open(f"{File}", "r") as file:
        Data = file.read()
    print(f"#### START \"{File}\" ####")
    print(Data)
    print(f"#### END \"{File}\" ####")
    print("Program ending.")
    return None
main()