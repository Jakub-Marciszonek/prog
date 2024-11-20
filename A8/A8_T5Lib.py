import hashlib

def menu1():
    print("Options:\n1 - Login\n2 - Register\n0 - Exit")
    Choice = input("Your choice: ")
    return Choice

def menu2():
    print("User menu:\n1 - View profile\n2 - Change password\n0 - Logout")
    Choice = input("Your choice: ")
    return Choice

def HashingPass(Password):
    Password = Password.encode()
    md5 = hashlib.md5()
    md5.update(Password)
    Password = md5.hexdigest()
    return Password

def Reg():
    Username = input("Insert username: ")
    Password = input("Insert password: ")
    Password = HashingPass(Password)

    with open("A8/credentials.txt", "a") as file:
        file.write(f"{Username};{Password}\n")

    print("User registration completed!")

def Log():
    Username = input("Insert username: ")
    Password = input("Insert password: ")
    Password = HashingPass(Password)

    Key = f"{Username};{Password}\n"
    ID = 0
    with open("A8/credentials.txt", "r") as file:
        for row in file:
            if row == Key:
                print("Authentication successful!")
                return ID
            ID +=1
        print("Authentication failed!")
        return -1

def ProfView(ID, row):

    Username = row[0]

    print(f"Profile ID {ID} - {Username}")

def UserFinder(ID):
    Line = 0

    with open("A8/credentials.txt", "r") as file:
        for i in file:
            if Line == ID:
                row = i.split(";")
                return row
            else:
                Line += 1

def PassChange(row):
    data = []

    NewPass = input("Insert new password: ")
    NewPass = HashingPass(NewPass)

    row[1] = NewPass

    with open("A8/credentials.txt", "r") as file:
        for i in file:
            data.append(i)

    for i in data:
        i.split(";")
        if i[0] == row[0]:
            i = row
        i = "".join(i)
    data = "".join(data)

    with open("A8/credentials.txt", "w") as file:
        file.write(data)
    return
