# Asuku CIS101 Oct10th with Io Cheng 
# This function will check each letter whether vowel or consonants or others by using if sentence
# In order to check each letter, this program use for loop, then check each letter.
# if a letter is vowel or consonants, those counts are plused 1 and stock the letter in each variable.
def tool(string):
  vowels=''
  consonants=''
  Vnum=0
  Cnum=0
  for i in string:
    if i.lower() in 'aiueo':
      vowels = vowels+i
      Vnum+=1
    if i.upper() not in'AIUEO1234567890!@##$%^&*()_+{}:"<>?-=[];,./ ':
      consonants = consonants+i
      Cnum+=1
  Vnum = String(Vnum)
  Cnum = String(Cnum)
  print 'Vowels:'+vowels+' Total vowels='+Vnum
  print 'Consonants:'+consonants+' Total vowels='+Cnum
tool("Matthew 7:7 Ask, and it shall be given you; seek, and ye shall find; knock, and it shall be opened unto you:")
# This function can input spaces between each letter as many as you want.
# First, This program prepare the space, then by using for loop, space and each letter will be combined.
def  spaceItOut(string,num):
  space=' '*num
  sentence=''

  for i in string:
    sentence =sentence+i+space
  print sentence
  
spaceItOut("It was a wonderful Beach Day at Hukilau Beach!", 2)