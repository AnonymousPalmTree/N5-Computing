#Party Costs - structure diagrams

child_buffet = 2

choice = str(input("Is cake required?"))
if choice =="yes" or "Yes" :
    cake = 15

if choice =="no" or "No" :
    cake = 0

adults = int(input("Input number of adults."))
children = int(input("Input number of children."))

dietary_requirements = []
for index in range(children):
    dietary_requirements = str(input("List [child]s dietary requirements."))

if adults + children >20:
    venue = 0

if adults + children <20:
    venue = 50

cost = ((child_buffet * children) + cake + venue)

print("the cost is £",cost, ".")

