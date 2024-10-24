def main():
    print("Program starting.")

    File1 = input("This program can copy a file.\nInsert source filename: ")
    File2 = input("Insert destination filename: ")
    with open(f"{File1}", "r") as file:
        content = file.read()
    print(f"Reading file '{File1}' content.")
    print("File content ready in memory.")
    print(f"Writing content into file '{File2}'.")
    with open(f"{File2}", "w") as file:
        file.write(content)
    print("Copying operation complete.")
    print("Program ending.")
    return None
main()