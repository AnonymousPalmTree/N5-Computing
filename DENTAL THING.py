#gc
#21/9/2023
#Dental Fillings

print("Dental Fillings")
print()

print("""

Your choices are :
           1. Temporary - £8
           2. Amalgam - £14
           3. White - £43
           4. Super White - £67
""")

choice = int(input("Enter either 1, 2, 3 or 4 to choose: "))
number = int(input("How many do you want to buy?"))
if choice==1:
    cost = number * 8
if choice==2:
    cost = number * 14
if choice==3:
    cost = number * 43
if choice==4:
    cost = number * 67

print("The cost is", cost, "pounds")
