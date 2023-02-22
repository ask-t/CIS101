# Asuku  CIS 101  November 2022  Assignment 29
# This function will open, read and close the file. Then it is count how many sentence are there. 
# This function will also count how many the number of uppercase, lowercase, and consonants by using if sentence.
# This function use while loop, so unless you input 'quit' it will keep working after finish the process.
def function ():
  while True:
    path = input('Enter path and file name (with quotes): ')
    if path =='quit':
      break
    file = open(path,"rt")
    contents = file.read()
    file.close()
    sentences = upper = lower = consonants = 0
    for i in contents:
    # ord 65 - 90 are Uppercase English alphabet letters
      if i in ".?!":
        sentences += 1
      if ord(i) >= 65 and ord(i)<= 90:
        upper += 1
        if i.lower()  not in 'aeiou':
          consonants +=1
    # ord 97 - 122 are Uppercase English alphabet letters 
      elif ord(i) >= 97 and ord(i)<= 122:
        lower += 1
        if i.lower()  not in 'eaoiu':
          consonants +=1
    print("The file contains "+str(sentences)+" sentences, "+str(upper)+"uppercase letters, "+str(lower)+"  lowercase letters, and "+str(consonants)+" consonants. ")