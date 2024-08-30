#g.c
#14/9/2023
#Average Calories

print('Weekly Calories')
print()

total=0
for day in range(7) :
    calories = int(input('Number of Calories consumed?'))
    total = total + calories

average = total/7
print()
print('Your average consumption was', average, 'Calories')


