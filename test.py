grid = [
[" ", "|", " ", "|", " "],
["-", "*", "-", "*", "-"],
[" ", "|", " ", "|", " "],
["-", "*", "-", "*", "-"],
[" ", "|", " ", "|", " "]
]
player = 1
while True:
    for lines in grid:
        for symbols in lines:
            print (symbols, end = "")
        print ("")