def main():

    print("Calculate fuel consumption.")
    Feed = input("Enter travel distance(kilometers): ")
    Distnance = int(Feed)
    Feed = input("Enter fuel usage(liters): ")
    FuelUsage = int(Feed)
    Consumption = int((FuelUsage / Distnance) * 100)

    print("Fuel consumption is", Consumption, "l per 100 km")

main()    