# Final

[Final Exam Study Guide.pdf](Final%20174d71e3a6714626a5875816e7959720/Final_Exam_Study_Guide.pdf)

Final Exam Study Guide CIS 101 Fall 2022
Final Exam - P2 This is the only time the Final Exam may be taken. You must use the classroom
computers in P2 and Canvas. This exam is closed internet and closed JES, no programming
tools, and no external websites. You may use scratch paper, the 'Python Tool Box" and your
notes. Dress and Grooming Standards will be enforced.
Topics to study:

### What are the differences between data types: integer, float, string?

**Integer ( int ): represents positive or negative whole numbers like 3 or -512.**
 **Floating point number ( float ): represents real numbers like 3.14159 or -2.5**
. Character string (usually called “string”, str ): text. Written in either single quotes or double quotes (as long as they match).

### Know how to use the math and modul operators.

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled.png)

### What are the reserved words in Python used for? (def, print, for, in, if, else, elif, and, or, not, while, break, continue, import, return)

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%201.png)

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%202.png)

## Be able to understand and explain a sequence of Python instructions.

We have been introduced to three Python types that are sequential in nature: **strings, lists, and tuples**. Among these, lists are the only mutable objects.

```python
mylist = list(range(10))
print(mylist)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# インデックスによるアクセス
n = mylist[1]  # 正数は先頭からのインデックス。先頭の要素のインデックスが0
print(n)  # 1
n = mylist[-2]  # 負数は末尾からのインデックス。末尾の要素のインデックスが-1
print(n)  # 8

# インデックスを使った要素の削除
del mylist[4]
print(mylist)  # [0, 1, 2, 3, 5, 6, 7, 8, 9]

# インデックスを使って要素を変更する
mylist[-1] = 90
print(mylist)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 90]

s = mylist[0:5]  # 0～4番目の5要素を取り出す
print(s)  # [0, 1, 2, 3, 4]

s = mylist[:]  # 全要素を取り出す
print(s)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

s = mylist[5:]  # 5番目以降の全要素を取り出す
print(s)  # [5, 6, 7, 8, 9]

s = mylist[:5]  # 0～4番目の5要素を取り出す
print(s)  # [0, 1, 2, 3, 4]

s = mylist[0:10:2]  # 0、2、4、6、8番目の要素を取り出す
print(s)  # [0, 2, 4, 6, 8]
```

## How does the + operator work among strings and numbers?

```python
a = 23
b = 'Hello'

print(b + a)

TypeError: can only concatenate str (not "int") to str
```

### How does the * operator work among strings and numbers?

```python
a = 'Alice' * 4 
print(a)
#'AliceAliceAliceAlice
```

## How do you create a comment in Python?

```python
# this is a comment
```

## Know how to use the range function with 1, 2, or 3 arguments.

```python
range(8)
#[0,1,2,3,4,5,6,7]

range(1,10)
#[1,2,3,4,5,6,7,8,9]

range(1,11,2)
#[1,3,5,7,9]

range(10,0,-1)
#[10,9,8,7,6,5,4,3,2,1]

string =  "0123456789ABCD"
print string[12]
#What will be printed?
#'C'

```

## Look at an incorrectly written function, and fix it.

### Example

```python
from random import randint

def highLow():
    print 'High Low Matching Game.'
    print 'Choose a number between 1 and 100 and try to match'
    print 'the random number with the fewest number of quesses.'
    
    x = 1; y = 100
    while true:
        rNum = randint(x,y)
        guessCnt = 0
        guess = 0
        guessCnt += 1
        
        while guess != rNum:
            guess=int(input('Guess # between'+str(x)+' and '+str(y)+':'))
            if guess > rNum:
                print 'Too high, guess again'
            elif guess < rNum:
                print 'Too low, guess again'
        print 'Correct, it took you', guessCnt, 'tries'
        
        playAgain = input("Play again? Enter 'y' or 'n': ")
        if playAgain == 'y':
            continue
        elif playAgain == 'n':
            break
    
    print 'Game ended..'
```

### First check print()

```python
❌print 'High Low Matching Game.'
⭕️print ('High Low Matching Game.')
```

### Second check while true

```python
❌ while true:
⭕️ while True:
```

### Check the position of variable for the counting

```python
while true:
	rNum = randint(x,y)
	guessCnt = 0
	guess = 0
	❌guessCnt += 1
        
  while guess != rNum:
	  guess=int(input('Guess # between'+str(x)+' and '+str(y)+':'))
	  if guess > rNum:
	    print 'Too high, guess again'
	  elif guess < rNum:
      print 'Too low, guess again'
```

### After modifing

```python
while true:
	rNum = randint(x,y)
	guessCnt = 0
	guess = 0
	guessCnt += 1
        
  while guess != rNum:
	⭕️guessCnt += 1
	  guess=int(input('Guess # between'+str(x)+' and '+str(y)+':'))
	  if guess > rNum:
	    print 'Too high, guess again'
	  elif guess < rNum:
      print 'Too low, guess again'
```

### Check random function

randint is imported from random function, so you need to add random before randint

```python
❌rNum = randint(x,y)
⭕️rNum = random.randint(x,y)
```

## Look at a function and describe what it does and how it works.

## How do you compute the length of a list or string?

```python
a = ['a','b','c','d']
b = 'Hello'

print(len(a))
print(len(b))

# 4
# 5
```

### How do you test for equality/inequality in Python?

```python
a = 'ABUiuO'

for i in a:
  if i == i.upper():
    print('true')
  else:
    print('false')

'''
true
true
true
false
false
true
'''
```

### Know how to use if, elif, and else.

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%203.png)

```python
string = ('1. This is a simple text file '
'with very few lines in it. '
'2. It contains mostly lowercase '
'letters, and a few UPPERCASE '
'letters also a couple of numbers. ')

def function (string):
  length = len(string)
  E = 0
  e = 0
  i = 0
  numbers = 0
  for j in string:
    if j == 'E':
      E +=1
    elif j == 'e':
      e += 1
    elif j == 'i':
      i += 1
    elif j in '1234567890':
      numbers+=1
		else:
			continue
  print("The file contains "+str(length)+" characters, "+str(E)+" 'E' characters, "+str(e)+" 'e' characters, "+str(i)+" 'i' characters and "+str(numbers)+" number characters.")

function (string)

# The file contains 152 characters, 2 'E' characters, 15 'e' characters, 9 'i' characters and 2 number characters.
```

### Use and, or, and not to build complex decisions.

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%204.png)

### Know how to use indexing to look up individual characters within a string.

use ‘in’

```python
a = 'pineapple'

for i in a:
  if i in 'apple':
    print('true')
  else:
    print('false')

'''
true
false
false
true
true
true
true
true
true
'''
```

### Know how to "slice" a string.

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%205.png)

```python
mylist = list(range(10))
print(mylist)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

s = mylist[0:5]  # 0～4番目の5要素を取り出す
print(s)  # [0, 1, 2, 3, 4]

s = mylist[:]  # 全要素を取り出す
print(s)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

s = mylist[5:]  # 5番目以降の全要素を取り出す
print(s)  # [5, 6, 7, 8, 9]

s = mylist[:5]  # 0～4番目の5要素を取り出す
print(s)  # [0, 1, 2, 3, 4]

s = mylist[0:10:2]  # 0、2、4、6、8番目の要素を取り出す
print(s)  # [0, 2, 4, 6, 8]
```

### Know how to use shortcut operators such as +=, -=, *=, /=

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%206.png)

### Be familiar with the names and behaviors of Python methods for string processing.

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%207.png)

### Know the difference between a for loop and a while loop.

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%208.png)

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%209.png)

### Convert a for loop to a while loop.

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%2010.png)

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%2011.png)

### Convert a while loop to a for loop.

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%2012.png)

### Know how to create an "infinite" while loop.

Don’t write any condition and break, just write True.

```python
while True:
	count += 1 
```

### Know how to "break" out of a loop early.

Use break

```python
while True:
	break
```

### What three things does every while loop need?

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%2013.png)

### Look at a loop, and determine how many times it will run.

### Know what makes “efficient” code.

```python
if char in "AEIOUaeiou":
#1  if char.lower() in "eaou":

if ASCII in range (97, 123, 1):
#2 if ASCII >= 97 and ASCII <123:

if character in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
#3  if 65<=ord(character.upper())<=90:

if credits in range (0, 30, 1):     # credits is a positive integer
#4 if int(credits)>=0 and int(credits)<30:

if char == '!' or char == '?' or char == '.':
#5  if char in ".?!":

```

### Know how to use the file open function and the file read and close methods.

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%2014.png)

```python
path = '/Users/ask/CIS101/input1.txt'
file = open(path,"rt")
contents = file.read()
file.close()
```

### Know how to use the sys list “argv” to pass arguments to Python from the command line.

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%2015.png)

```python
from sys import argv

a=int(argv[0])
b=int(argv[1])
c=int(argv[2])
d=int(argv[3])
e=int(argv[4])

a = 'Assign35.py'
b = 'W'
c = '3'
d = '2'
e = '2'

```

### Use import to access functions from modules. Match vocabulary words to their definitions:

### string

A sequence of characters. 

### string concatenation: Joining two or more shorter strings together to form a longer string.

### string duplication

```python
Alice' * 4 returns 
# 
'AliceAliceAliceAlice'
```

### variable:

The name for data.

### function:

A sequence of instructions that is assigned a name.

### algorithm:

A step-by-step description of a process that is not a computer program.

### program:

An algorithm that is written in a computer language.

### parameter / argument:

Data that is passed to a function.

### comment

```python
# comment out 
```

### reserved word:

A word or combination of letters that is defined by Python and may not be used as a variable or function name.

### block

### path

### loop

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%2016.png)

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%2017.png)

### for:

a loop that "loops" through a list of values

### while:

a loop that "loops" as long as its condition is true

### break:

end the loop (execute statement after the loop)

### continue:

stop the current iteration of a loop and start at top of loop with next iteration

### path separator

For windows, we use \.  For Mac, we use / 

### encoding

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%2018.png)

### list

### bug

**an unexpected problem**

### bit :

a "bit" is atomic: the smallest unit of storage. A bit stores just a 0 or 1

```python
How many numbers can you represent with three binary digits (bits)?
# 8

How many numbers can you represent with five bits?
# 32

What are the smallest and largest numbers (converted to decimal) in 4 binary bits?   (all 0's and all 1's)
# 0 and 15

What are the smallest and largest numbers (converted to decimal) in 2 binary bits?   (all 0's and all 1's)
# 1 and 4

How many bits are in a byte?
# 8
```

### byte :

One byte = collection of 8 bits

### return:

The Python return statement is **a special statement that you can use inside a function or method to send the function's result back to the caller**.

### if / elif / else:

test whether a given condition is true, and run a block of code if it is.

### command-line argument

```python
python filename.py
```

### method

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%2019.png)

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%2020.png)

### Import:

import all functions in module

![Untitled](Final%20174d71e3a6714626a5875816e7959720/Untitled%2021.png)
