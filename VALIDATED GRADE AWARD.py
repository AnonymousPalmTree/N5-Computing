#g.c
#12/10/2023
#Grade Award

print('Grade Award Program')
print()

name = input("Please enter your name: ")

# validated input of number
mark = int(input("Please enter the mark out of 100: "))
while mark<0 or mark>100:
    print("ERROR,", mark, "is not a recognised mark")
    mark=int(input("Please enter the mark out of 100: "))

print()

if mark < 100 >= 70 :
    grade = 'A'

if mark < 70 >= 60 :
    grade = 'B'
    
if mark < 60 >= 50 :
    grade = 'C'

if mark < 50 >=40 :
    grade = 'D'

if mark < 40 >=0 :
    grade = 'F'

print("you got", mark, "% and a grade", grade)




