#Asuku CIS101Sec3 Assigin27
# First, in order to read the txt file, we can use open() and read(), 
# then make variable and put the content of txt in the variable.
# After that, prepare some variables to count the number how many specific letters are there. 
# By using for loop, count numbers then show the information.
path = '/Users/ask/CIS101/input1.txt'
file = open(path,"rt")
contents = file.read()

def function (string):
  length = len(string)
  E = e = i = numbers = 0
  for j in string:
    if j == 'E':
      E +=1
    elif j == 'e':
      e += 1
    elif j == 'i':
      i += 1
    elif j in '1234567890':
      numbers+=1
  print("The file contains "+str(length)+" characters, "+str(E)+" 'E' characters, "+str(e)+" 'e' characters, "+str(i)+" 'i' characters and "+str(numbers)+" number characters.")
function (contents)

