#g.c
#14/9/2023
#Tuck Shop

print("""
Your choices are:
                   1. Crisps at £50
                   2. Cans at £80
                   3. Chocolate at £70
                   4. Water at £40
""")
choice = int(input("Enter either 1, 2, 3 or 4 to choose: "))
number = int(input("How many do you want to buy?"))
if choice==1 :
    cost = number * 50
    
if choice==2 :
    cost = number * 80
    
if choice==3 :
    cost = number * 70
    
if choice==4 :
    cost = number * 40

print("The cost is = £", cost)
    
    
