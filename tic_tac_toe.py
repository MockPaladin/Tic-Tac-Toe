game_history = ""
numbered_grid = [["1", "|", "2", "|", "3"],["-", "*", "-", "*", "-"],["4", "|", "5", "|", "6"],["-", "*", "-", "*", "-"],["7", "|", "8", "|", "9"]]
grid = [[" ", "|", " ", "|", " "],["-", "*", "-", "*", "-"],[" ", "|", " ", "|", " "],["-", "*", "-", "*", "-"],[" ", "|", " ", "|", " "]]
go_on = False
player = 1
def place_in_grid(where_to_put_bob,bob):


    global grid, go_on

    if where_to_put_bob == 1:
        grid[0][0] = bob
        go_on = True
    elif where_to_put_bob == 2:
        grid[0][2] = bob
        go_on = True
    elif where_to_put_bob == 3:
        grid[0][4] = bob
        go_on = True
    elif where_to_put_bob == 4:
        grid[2][0] = bob
        go_on = True
    elif where_to_put_bob == 5:
        grid[2][2] = bob
        go_on = True
    elif where_to_put_bob == 6:
        grid[2][4] = bob
        go_on = True
    elif where_to_put_bob == 7:
        grid[4][0] = bob
        go_on = True
    elif where_to_put_bob == 8:
        grid[4][2] = bob
        go_on = True
    elif where_to_put_bob == 9:
        grid[4][4] = bob
        go_on = True
    else: print ("try again") 

def player_move(bob):
    global go_on, game_history

    while go_on == False:

            where_to_put_bob = input(f"Choose where you'd like to place your {bob} (1 is top left, 9 is bottom right, type [D] for description, [G] is game history): ")
            
            
            
            if where_to_put_bob.upper() == "D":
                for lines in numbered_grid:
                    for individual_characters in lines: print (individual_characters, end = " ")
                    print ("")
            elif where_to_put_bob.upper() == "G": print (game_history)
            else:

                game_history += where_to_put_bob
                where_to_put_bob = int(where_to_put_bob)
                place_in_grid(where_to_put_bob, bob)

    go_on = False

while True:

    if player == 1:
        player_move("X")
        player = 2
    else: 
        player_move("O")
        player = 1

    for lines in grid:
        for symbols in lines:
            print (symbols, end = "")
        print ("")
