import random

lstNames = ['COMPUETR','KEYBOARD','PRINTER','SCANNER','MOUSE','LABORATORY','DATA','JOYSTICK','TRACKPAD','WEBCAM','LIGHTPEN','MONITOR','PROJECTOR','PROCESSOR']
name = random.choice(lstNames)
strlen = len(name)


print('HANGMAN')
print('You require to trace a Word related to COMPUTER by guessing characters')
print('You have 15 turns')
print('The word you got to trace has {0} alphabets in it'.format(strlen))

def check(alpha):
    if len(alpha) == 1 and alpha.isalpha() :
        return True

i = 0
k = 0
while i < 15 :
    alpha = input('Enter a Character : ')
    alpha = alpha.upper()

    if check(alpha) :
        j = 1
        for s in name :
            if alpha == s :
                print('Found : Character {0}  Position {1} '.format(alpha,j))
                k = k+1
                if k == strlen :
                    print('You Win \n The word is {}'.format(name))
                    exit()
            else : 
                pass
            j = j+1
        i=i+1
        if i == 15 :
            print('You lost \n The Word is {}'.format(name))

    else :
        print('Error!!! \nEnter a single English alphabet')
    
    