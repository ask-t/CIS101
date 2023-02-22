# Asuku  CIS 101   Nov28th Assignment35
# This program prints flags. you can change the size, letter, by inputing the number on terminal or command line.
# There are two functions. First one is making the flag. By using a letter and number how big you want to make, it is possibe to make flag with for loop
# And second one is making pole it is also using for loop.
# Usage:py flagPole.py flagCharacter flagSize poleLength numberOfFlags

# import argv from sys (argv is a list)
from sys import argv
#  functions defined:
# This function prints a flag made of a character and size
def flag(flagChar,flagSize):
    for i in range(1,flagSize+1):
        print("|"+(flagChar*i))

# This function prints a flag pole of length
def pole(poleLength):
    for i in range(poleLength):
        print ("|")
# main program
#  initialize variables from system argv
fChar=argv[1]
fSize=int(argv[2])
pLen=int(argv[3])
numF=int(argv[4])
# By using range, show the flags as many as you want.
for _ in range(numF):
  flag(fChar,fSize)
  pole(pLen)
# code to print flags
# End of program



