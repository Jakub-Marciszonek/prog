DELIMITER = ","
def collectWords():
    PList = []
    while True:
        PWord = input("Insert word(empty stops): ")
        if PWord == "":
            break

        PList.append(PWord)
        for i in PList:

            Pword = "".join(PList)
        PList.append(DELIMITER)

    return Pword

def analyseWords(Dupa: str):

    NrWords = Dupa.count(",") + 1
    NrCharacters = len(Dupa) - Dupa.count(",")
    Avg = NrCharacters / NrWords
    print(f"- {NrWords} Words")
    print(f"- {NrCharacters} Characters")
    print("- {:.2f} Average word length".format(Avg))

def main():
    print("Program starting.")
    Word = collectWords()
    analyseWords(Word)

    print("Program ending.")
    return None
main()