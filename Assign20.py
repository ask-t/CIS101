def mixEm1(string):
    mix = ""
    for index in range(0, len(string), 4):
        mix = mix + string[index]
        mix = mix + "_"
        for indexA in range(len(string)/4, len(string)/2, 2):
            mix = mix + string[indexA]
    print (mix)

def mixEm2(string):
    mix = ""
    for index in range(len(string)/4):
        mix = mix + string[index] + "."
        for indexA in range(len(string)-6 ,len(string)):
            mix = mix + string[indexA]
        mix = mix + "."
    print (mix)
 
def mixEm3(string):
    mix = ""
    for index in range(0, len(string)/3, 2):
        mix = "$" + string[index] + mix
        for indexA in range(len(string)/2, len(string), 5):
            mix = mix + string[indexA]
    print (mix)
    
def mixEm4(string):
    for letter in string:
        mix = " " + letter + " "
        for index in range(len(string) - 1, -1, -1):
            mix = string[index] + mix + string[index]
        print(mix) 