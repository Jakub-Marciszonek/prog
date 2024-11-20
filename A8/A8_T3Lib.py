def Readfile():
    List = []
    Filename = input("Insert filename: ")
    with open(Filename, "r") as file:
        for i in file:
            i = i.removesuffix("\n")
            if i != "":
                i = float(i)
                List.append(i)
    return List


