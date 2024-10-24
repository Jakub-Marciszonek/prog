print("Program starting.")
print("Estimate how many minutes you spent on programming...\n")

T1 = float(input("A1_T1: "))#i have no idea how to do it diffrently as much as i want 
T2 = float(input("A1_T2: "))#to know i propably forget cuz its late and im litteraly
T3 = float(input("A1_T3: "))#falling a sleep
T4 = float(input("A1_T4: "))
T5 = float(input("A1_T5: "))
T6 = float(input("A1_T6: "))
T7 = float(input("A1_T7: "))
list = [T1, T2, T3, T4, T5, T6, T7] #list for grouping data 
#I tried use class but idk how so i abondoned the idea XD
Total = int(sum(list))
Avg = round((sum(list)/len(list)), 2)

print(f"\nIn total you spent {Total} minutes on programming.")
print(f"Average per task was {Avg} min and same rounded to the nearest\
 integer {round(Avg)} min.")

print("\nProgram ending.")