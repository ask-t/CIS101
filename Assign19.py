def mixIt1(number):
      letters = 'abcdefghijklmnopqrstuvwxyz'
      pile = ""
      for index in range(0, number):
            pile = letters[index] + pile + letters[index]
      print pile

def mixIt2(number):
      letters = 'abcdefghijklmnopqrstuvwxyz'
      pile = ""
      for index in range(12, len(letters), len(letters) % number):
            pile = pile + letters[index]
      print pile

def mixIt3(number):
      letters = 'abcdefghijklmnopqrstuvwxyz'
      pile = ""
      for index in range(1, len(letters) / 2):
            pile = letters[number % index] + pile
      print pile
      
def mixIt4(number):
      letters = 'abcdefghijklmnopqrstuvwxyz'
      pile = ""
      for index in range(0, len(letters), 4):
            pile = pile + letters[index % number]
      print pile

