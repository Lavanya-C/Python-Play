import math
import random

ran = random.randrange(0,1000,1)

print('Try guessing number randomly between range 0-1000')
print('You have 10 turns')

def diff(a ,b):
    return a-b

i=0
while i < 15 :
    num = (input('Enter the number : '))

    if num.isdigit() :
        num =int(num)
        
        if ran == num:
            print('You win')
            print('Congratulations')
            exit()
        elif num < ran:
            print('You have entered a smaller number')
            sub = diff(ran, num)
            if num < sub :
                print('The DIFFERENCE is HIGH ')
            elif num > sub :
                print('The DIFFERENCE is LESS ')
            else :
                print('The DIFFERENCE is equal to NUMBER ')
        else :
            print('You have enterted a greater number')
            sub = diff(num, ran)
            if num < sub :
                print('The DIFFERENCE is LESS ')
            elif num > sub :
                print('The DIFFERENCE is HIGH ')
            else :
                print('The DIFFERENCE is equal to NUMBER ')

        print('Try Again')
        i=i+1
        if i==15 :
            print('You Lost \nThe Generated RANDOM NUMBER is : ',ran)
    else :
        pass