def modify(string):
    target = ""
    for letter in string:
        target = letter+target
    print target
modify("rubber duck")