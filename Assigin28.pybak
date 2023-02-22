def function ():
  while True:
    path = input('Enter path and file name (with quotes): ')
    if path =='quit':
      break
    file = open(path,"rt")
    contents = file.read()
    sentences = upper = lower = consonants = 0
    list_contents = contents.split()
    sentences = len(list_contents)
    for i in contents:
      if ord(i) >= 65 and ord(i)<= 90:
        upper += 1
      if ord(i) >= 97 and ord(i)<= 122:
        lower += 1
      if i.lower()  not in 'aiueo':
        consonants +=1
    print("The file contains "+str(sentences)+" sentences, "+str(upper)+"uppercase letters, "+str(lower)+"  lowercase letters, and "+str(consonants)+" consonants. ")
    break

function ()