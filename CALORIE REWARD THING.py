#gc
#7/9/2023
#Calorie Reward

print("Calorie Reward thingy")
print()

breakfast_calories = int(input("How many calories did you consume at breakfast?"))
lunch_calories = int(input("How many calories did you consume at lunch?"))
dinner_calories = int(input("How many calories did you consume at dinner?"))

total_calories = dinner_calories + lunch_calories + dinner_calories

print("You have consumed", total_calories)

calories_burnt = int(input("How many calories did you burn"))

net_loss = calories_burnt - total_calories

if net_loss >= 100 :
    print("Good job")

if net_loss <= 100 :
    print("uagyisgyigygy")

