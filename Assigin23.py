#Asuku CIS101sec3 Assign23

# show char as many as you want with for loop
def textRectanagle(char, width, height):
  for _ in range(height):
    print char*width
    
# textRectanagle("M", 8, 6)

# show the char as many as you want at the first and last line.
# At other lines, it shows the line char add space as much as width - 2  and add char.
#those process is worked by for loop
def textRectanagle2(char, width, height):
  print width * char
  for i in range(height-2):
    print char + (width-2) * " " + char
  print width * char
  
# textRectanagle2("M", 8, 6)

# At second and third line is including space
# others are just showing char as many as you want.
#By using for loop, you can show the line as many as you want.
def textRectanagle3(char, width, height):
  print width * char
  for i in range(2):
    print char + (width-2) * " " + char
  for i in range(height-3):
    print width * char
#textRectanagle3("M", 8, 6)

#First line is show the char as many as width.
#Second line consint of char as many as num.At this time num is 2.  
#And spaceas many as width -3  and a char.
#Num plus 2 because, third line's first char are 4.
#Num plus 1, then, follow same process.

def textRectanagle4(char, width, height):
  num = 2 
  print width * char
  print char*num +(width-(num+1)) * " " + char
  num +=2
  print char*num +(width-(num+1)) * " " + char
 
  for i in range(height -3):
    num +=1
    print char*num+(width-(num+1)) * " " + char
    
textRectanagle4("M", 8, 6)