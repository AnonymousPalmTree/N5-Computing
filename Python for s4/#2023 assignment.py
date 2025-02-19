#2023 assignment 
# task1

jureny_stage_costs = []
totalMiles = 0
totalCost = 0

numStations = int(input("How many charging stations????? "))
startMiles = int(input("What mile yuo on rn ?????? "))

#input validation
for stations in range (numStations):
    currentMiles = int(input("hOW MANY MILE at this chraging station ?????? "))
    kwRating = int(input("HOW MANY KILOWAT ?????????????????????????? "))
    while kwRating != 7 and kwRating != 22 and kwRating != 50:
        kwRating = int(input("ERROR IVALID INPUT!! PLEASE!! HOW MANY KILOWAT ?????????????????????????? "))
    if kwRating == 7:
        price == 0
    elif kwRating == 22:
        price == 0.005
    elif kwRating == 50:
        price == 0.01
    
    #processes
    milesTraveled = currentMiles - startMiles
    totalMiles = totalMiles + milesTraveled
    startMiles = currentMiles
    #1d arrays
    journeyStageCost = price * milesTraveled
    jureny_stage_costs.append(journeyStageCost)

station = 0
for index in range (numStations) :
    totalCost = totalCost + jureny_stage_costs[index] 
    station = station +1
    print("CHARGIN STATION", station, "COST U £",round(jureny_stage_costs[index],2))

#display total miles and total cost
print("UR jorueny cpst u £",round(totalCost,2), "ans u travveld totally",round(totalMiles,2), "miles")