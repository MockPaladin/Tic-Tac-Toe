from time import sleep
x_or_o = 1
grid = [
[" ", "|", " ", "|", " "],
["-", "*", "-", "*", "-"],
[" ", "|", " ", "|", " "],
["-", "*", "-", "*", "-"],
[" ", "|", " ", "|", " "]]
x_counter = 0
o_counter = 0
game_history_input = input("Paste your game history here: ")

def check_game():

    
    global grid, x_or_o
    
    for where_to_put_bob in game_history_input:

        if x_or_o == 1:
            char = "X" # 'char' is short for character
            x_counter += 1
        else:
            char = "O"
            o_counter += 1

        if where_to_put_bob == "1": grid[0][0] = char
        elif where_to_put_bob == "2": grid[0][2] = char
        elif where_to_put_bob == "3": grid[0][4] = char
        elif where_to_put_bob == "4": grid[2][0] = char
        elif where_to_put_bob == "5": grid[2][2] = char
        elif where_to_put_bob == "6": grid[2][4] = char
        elif where_to_put_bob == "7": grid[4][0] = char
        elif where_to_put_bob == "8": grid[4][2] = char
        elif where_to_put_bob == "9": grid[4][4] = char
        else: print ("something went wrong")

        if x_or_o == 1: x_or_o = 2
        else: x_or_o = 1
        for lines in grid:
            for characters in lines: print (characters, end = " ")
            print("")
        sleep(2)

check_game()
print ("The end of your game looked like this:")
for lines in grid:
    for characters in lines: print (characters, end = " ")
    print ("")
print (f"It lasted {len(game_history_input)} moves, with {x_counter} moves from Player One, and {o_counter} moves from Player Two!")