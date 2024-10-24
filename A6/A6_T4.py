def main():
    print("Program starting.")
    List = []
    Total = 0
    Filename = input("This program analyses a list of names from a file.\nInsert filename to read: ")
    print(f"Reading names from \"{Filename}\".")
    with open(f"{Filename}", "r") as file:
        Content = file.read()
    print("Analysing names...")
    Splited = (Content.split("\n"))
    for i in Splited:
        if i == "":
            continue
        else:
            List.append(i)
    NameCount = len(List)
    for i in List:
        Total += len(i)
    AVG = float(Total)/ float(len(List))

    print("Analysis complete!")
    
    print(f"#### REPORT BEGIN ####\nName count - {NameCount}\n\
Shortest name - {len(min(List, key=len))} chars\nLongest name - {len(max(List, key=len))} chars\n\
Average name - {AVG:.2f} chars\n#### REPORT END ####")
    print("Program ending.")
    return None
main()