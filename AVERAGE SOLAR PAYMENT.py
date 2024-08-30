#g.c
#14/9/2023
#Average Solar Payment

print('Average Solar Payment')
print()

total=0
for quarter in range(4) :
    payment = int(input('How much monies did you get given $$$$$'))
    total = total + payment

average = total/4
print()
print('Your average solar payment was £', average, 'dolla dolla bills')

    
    
