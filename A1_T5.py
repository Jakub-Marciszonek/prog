def main():


    print("Calculate the area of a wall.")
    Feed = input("Enter the width in meters: ")

    Width = float(Feed)
    Feed = input("Enter the height in meters: ")

    Height = float(Feed)
    print("Width is", Width, "m and height is", Height, "m.")

    Area = float(Width * Height)
    Area = round(Area, 2)
    print("The wall will be", Area, "square meters.")


main()

