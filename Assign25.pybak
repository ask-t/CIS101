#Asuku CIS101 sec3 Assign25
# First one is just showing the string.
#Second one is showing  the input string with every other word made uppercase. 
#In order to do that, By doing if sentence, and only odd numbers letter become upper. even numbers letter become lower.
#Last one is showing the string in reverse order. By using index number from biggest number to smallest,
#it is possibe to show string in reverse order.
def function(string):
  text =''
  num=0
  for i in string:
    if num%2 == 0:
      text = text+i
    num +=1
  print(text)
  list_a = string.split()
  txt =''
  num = 0
  for i in list_a:
    if num%2 == 0:
      i = i.upper()
    else:
      i.lower()
    txt = txt + i +' '
    num +=1
  print(txt)
  length = len(string)
  txt2 = ''
  for _ in range(length):
    length -=1
    txt2 = txt2+ string[length]
  print(txt2)

