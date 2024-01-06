grid = [
[" ", "|", " ", "|", " "],
["-", "*", "-", "*", "-"],
[" ", "|", " ", "|", " "],
["-", "*", "-", "*", "-"],
[" ", "|", " ", "|", " "]]
go_on = False
player = 1
def player_move(bob):

    global go_on

    while go_on == False:

            where_to_put_bob = input(f"Choose where you'd like to place your {bob} (1 is top left, 9 is bottom right): ")
            try: where_to_put_bob = int(where_to_put_bob)
            except: print ("bro it didnt work")

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
    