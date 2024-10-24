def frameWord(PWord):
    print(f"**{len(PWord) * "*"}**")
    print(f"* {PWord} *")
    print(f"**{len(PWord) * "*"}**")

def main():
    print("Program starting.")
    Text = str(input("Insert word: "))
    print("")
    frameWord(Text)
    print("")
    print("Program ending.")
    return None
main()