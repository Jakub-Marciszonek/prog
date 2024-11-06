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
    if List == []:
        print("No integers to display.")
        return
    print(f"Displaying {len(List)} integers:")
    for i in List:
        print(f"- Index {List.index(i)} => \
Ordinal {List.index(i)+1} => Integer {i}")

def main():
    print("Program starting.")
    displaydata(savingint())
    print("Program ending.")

main()