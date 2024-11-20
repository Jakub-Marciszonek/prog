def savingint():
    List = []
    print("Collect positive integers.")
    while True:
        No = input("Insert positive integer(negative stops): ")
        if "-" in No:
            print("Stopped collecting positive integers.")
            return List
        if No.isnumeric():
            No = int(No)
            List.append(No)

def displaydata(List):
    No0 = 0
    if List == []:
        print("No integers to display.")
        return
    print(f"Displaying {len(List)} integers:")
    for i in List:
        print(f"- Index {No0} => Ordinal {No0 + 1} => Integer {i}")
        No0 += 1

def main():
    print("Program starting.")
    displaydata(savingint())
    print("Program ending.")
    return None

main()