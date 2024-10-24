def askDimension(PPrompt: str) -> float:
    Feed = int(input(f"Insert {PPrompt}: "))
    return Feed

def calcRectangleArea(PWidth: float, PHeight: float) -> float:
    Area = (PWidth * PHeight)
    return Area

def main():
    print("Program starting.")
    Width = askDimension("width")
    Height = askDimension("height")

    Area = calcRectangleArea(Width, Height)

    print(f"\nArea is{Area: .1f}²")
    print("Program ending.")
    return None
main()