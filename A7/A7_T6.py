import random
random.seed(1234)

def booting():
    print("Welcome to the rock-paper-scissors game!")
    Name = input("Insert player name: ")
    print(f"Welcome {Name}!")
    print("Your opponent is RPS-3PO.")
    print("Game starts...\n")
    return Name

def menudisplay():
    print("Options:\n1 - Rock\n2 - Paper\n3 - Scissors\n0 - Quit game")
    UserChoice = int(input("Your choice: "))
    if UserChoice == 0:
        return 0
    print("Rock! Paper! Scissors! Shoot!\n")

    return UserChoice

def GameDisplay(Choice, Name):
    print("#########################")
    if Choice == 1:
        print(f"{Name} chose rock.")
        print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
        return "rock"
    if Choice == 2:
        print(f"{Name} chose paper.")
        print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
        return "paper"
    if Choice == 3:
        print(f"{Name} chose scissors.")
        print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
        return "scissors"

def jury(UserChoice, RPSbot, User, Bot, Name):
    if UserChoice < RPSbot and RPSbot - UserChoice == 1\
or UserChoice > RPSbot and UserChoice - RPSbot == 2:
        print("#########################\n")
        print(f"RPS-3PO {Bot} beats {Name} {User}.\n")
        Count = 1
    elif RPSbot < UserChoice and UserChoice - RPSbot == 1\
or RPSbot > UserChoice and RPSbot - UserChoice == 2:
        print("#########################\n")
        print(f"{Name} {User} beats RPS-3PO {Bot}.\n")
        Count = 2
    elif UserChoice == RPSbot:
        print("#########################\n")
        print(f"Draw! Both players chose {User}.\n")
        Count = 0
    return Count

def Counting(UCounter, Count):
    UC = [UCounter[0], UCounter[1], UCounter[2], UCounter[3], UCounter[4]]
    if Count == 1:
        UC[1] += 1
        UC[3] += 1
    elif Count == 2:
        UC[0] += 1
        UC[4] += 1
    else:
        UC[2] += 1
    return UC

def CounterDisplay(UCounter, Name):
    print("\nResults:")
    print(f"{Name} - wins ({UCounter[0]}), losses ({UCounter[1]}), \
draws ({UCounter[2]})")
    print(f"RPS-3PO - wins ({UCounter[3]}), losses ({UCounter[4]}), \
draws ({UCounter[2]})")

def main():
    print("Program starting.")
    UCounter = [0, 0, 0, 0, 0]
    Name = booting()
    while True:
        RPSbot = random.randint(1, 3)
        UserChoice = menudisplay()
        if UserChoice == 0:
            CounterDisplay(UCounter, Name)
            break
        User = GameDisplay(UserChoice, Name)
        Bot = GameDisplay(RPSbot, "RPS-3PO")
        Count = jury(UserChoice, RPSbot, User, Bot, Name)
        UCounter = Counting(UCounter, Count)
    print("\nProgram ending.")
    return None
main()