# Asuku CIS101 Oct7th Assignment
def sort(string):
  consonants=''
  vowels=''
  for i in string:
    if i.lower() in "aeiou":
      vowels = vowels+ i
    if i.lower() not in "aeiou1234567890,;: ":
       consonants = consonants+ i
  print ('Vowels: '+vowels)
  print ('Consonants: '+consonants)

sort("Matthew 7:7 Ask, and it shall be given you; seek, and ye shall find; knock, and it shall be opened unto you")