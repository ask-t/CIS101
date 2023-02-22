# Asuku CIS101Sec3 Assigin 26

# get a character from words with for loop.
# By using ord(), it exchange sentences to the number'
def secretMessage(string):
  text =''
  for i in string:
    text = text + str(ord(i))+' '
  print(text)
#secretMessage("The apartment key is in postage box #269")

#fetch only F,f,m,M then put on the valiable.
#counts how many letters in the sentence.
#separate between M and F.
# counts how many F and M are there.
#In order to get the average, devied the numer of F or M by length of a letter.
def percentGenders(data):
  text =''
  for i in data:
    if i == 'M'or i == 'm' or i == 'f' or i == 'F':
      text = text + i 
  print(text)
  length = len(text)
  male =0.0
  female=0.0
  for i in text:
    if i == 'm' or i =='M':
      male+=1  
    if i == 'f' or i =='F':
      female+=1   
  print(male,length,female)
  aveM = float(male/length*100)
  aveF = float(female/length*100)
  print('There are  '+str(aveF) +'% females  and '+str(aveM) +'% males')
  
#percentGenders("MFFmmMFFMFMFfFM")


#6 for y, 7 for u, 8 for i, 9 for o, 0 for p, y for h, u for j, i for k, o for l, h for n, and j for m.
# exchange a letter to specific a letter with above list.
#replace() can fix specific letters.
def  fixItUp(string):
  string=string.replace("h","n")
  string=string.replace('y','h')
  string=string.replace('6','y')
  string=string.replace("j","m")
  string=string.replace("u","j")
  string=string.replace("7","u")
  string=string.replace("i","k")
  string=string.replace("8","i")
  string=string.replace("o","l")
  string=string.replace("9","o")
  string=string.replace("0","p")
  print(string)
