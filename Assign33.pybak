# Asuku  CIS 101  November 2022  Assignment 33
# enter two numbers, then this function checked if the words which is entered number or not with unicode.
# After checking those and if those are number, then calculate those numbers. Then, showing the results.
def function ():
  while True:
    a = True
    X = input("Input a number. If you would like to quit, input 'q' >>> ")
    if X == 'q':
      break
    while a == True:
      for i in X:
        if ord(i) >= 48 and ord(i)<= 57:
          continue
        else:
          print ('Sorry, your input is incorrect, please enter a number ')
          a = False
          break
      if a == False:
        break
      Y = input('Input a number >>> ')
      for j in Y:
        if ord(j) >= 48 and ord(j)<= 57:
          continue
        else:
          print ('Sorry, your input is incorrect, please enter a number ')
          a = False
          break
      if a == True:
        x = int(X)
        y = int(Y)
        plus = x+y
        minus = x-y
        multiple = x*y
        divided = float(x)/float(y)
        print('X = '+ X, 'Y = '+ Y)
        print ( 'X + Y= '+str(plus)+ ' ,X-Y = '+str(minus)+' ,X * Y = '+ str(multiple) + ' ,X / Y = ' + str(divided) )
        break
