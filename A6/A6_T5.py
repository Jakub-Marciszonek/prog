def readNanalis():
    Filename = input("Insert filename: ")
    print("#### Number analysis - START ####")
    reading(Filename)
    print("#### Number analysis - END ####")


def reading(Filename):
    with open(f"{Filename}", "r") as file:
        Content = file.read()
    print(f"File \"{Filename}\" results:")
    analysis(Content)
    return Content

def analysis(Content):
    
    Splited = (Content.split("\n"))
    for i in Splited:
        if i == "":
            Splited.remove(i) 
    Splited = list(map(int, Splited))
    
    Count = len(Splited)
    Sum = sum(Splited)
    Greatest = max(Splited)
    Avg = Sum/Count
    print("Count;Sum;Greatest;Average")
    print(f"{Count};{Sum};{Greatest};{Avg:.2f}\n")
def main():
    print("Program starting.")
    readNanalis()
    
    print("Program ending.")
    return None
main()