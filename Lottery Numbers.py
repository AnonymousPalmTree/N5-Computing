#gc
#18/6/2024
#Lottery Numbers

#add array here

lottery_numbers = int(input("Input lottery number"))
while lottery_numbers<1 or lottery_numbers>49:
            print("Invalid!! The number", lottery_numbers, "is not within the allowed range of numbers 1-49")
            lottery_numbers = int(input("Input lottery number"))
                      
