# Asuku CIS101 Oct24th Engage/Assign: 21
def spaceWords(string, numSpaces):
  a = string.split()
  text = ''
  length = len(a)
  for i in a:
    space =''
    for j in range(numSpaces):
      space += ' '
    text =  text + i + space
  print(text)
  
  
  
spaceWords("For behold the field is white already to harvest.", 3)

spaceWords("For behold the field is white already to harvest.", 4)

spaceWords("For behold the field is white already to harvest.", 5)

spaceWords("For behold the field is white already to harvest.", 6)