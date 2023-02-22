# Asuku  CIS 101  Nov30th  Assignment36 
import random
from sys import argv
def highLow():
    print ('High Low Matching Game.')
    print ('Choose a number between 1 and 100 and try to match')
    print ('the random number with the fewest number of quesses.')
    x = int(argv[1]); y = int(argv[2])
    while True:
    # choose a number randomly
        rNum = random.randint(x,y)
        # count how many times people tried to guess
        guessCnt = 0
        # for inputting number
        guess = 0
        # it will keep working until people can answer the correct number
        while guess != rNum:
        # Everytime when people try to guess, guessCnt plus 1
            guessCnt += 1
            guess=int(input('Guess # between'+str(x)+' and '+str(y)+':'))
            if int(argv[1]) <=guess <= int(argv[2]):
            # if the inputting number is high
              if guess > rNum:
                  print ('Too high, guess again')
            # if the inputting number is low
              elif guess < rNum:
                  print ('Too low, guess again')
        print ('Correct, it took you', guessCnt, 'tries')
        # depending on the answer, the program will be decided to keep working or not.
        playAgain = input("Play again? Enter 'y' or 'n': ")
        if playAgain == 'y':
            continue
        elif playAgain == 'n':
            break
    print ('Game ended..' )
    
highLow()