#tic-tac game 2 player's game using X and O

#Display of tic-tac board

game_still_on = True


board = ['-','-','-',
         '-','-','-',
         '-','-','-']

#game is still going

def display():
    print(board[0],'|',board[1],'|',board[2])
    print(board[3],'|',board[4],'|',board[5])
    print(board[6],'|',board[7],'|',board[8])
    
#display()

    
# Postion on the board
def turn(player):
    position = input("Select the position from 1-9: "+player)
    position = int(position)-1
    if board[position] == "X" or board[position] == "O":
        turn(player)
    else:
       board[position] = player
       display()
        
    
    
def play_game():
    display()
    while game_still_on == True:
        turn("X")
        turn("O")
        cgston=check_if_win("O")
        ##print(cgston,"checked")
        if cgston==False:
            break
        

def check_if_game_over(player):
    check_if_win(player)
    

def check_if_win(player):
    game_still_on1 = 1
#check row
    if board[0]== player and board[1]== player and board[2]== player :
        print(player + " Win")
        game_still_on1= False
    elif board[3]== board[4] and board[4]== player and  board[4]== board[5]:
        print(player+ " Win")
        game_still_on1= False
    elif board[6]== board[7] and board[6]== player and  board[7]== board[8]:
        print(player + " Win")
        game_still_on1= False
#check column
    if board[0]== player and board[3]== player and board[6]== player :
        print(player + " Win")
        game_still_on1= False
    elif board[1]== board[4] and board[4]== player and  board[4]== board[7]:
        print(player+ " Win")
        game_still_on1= False
    elif board[2]== board[5] and board[5]== player and  board[5]== board[8]:
        print(player + " Win")
        game_still_on1= False
#check diagonal
    if board[0]== player and board[4]== player and board[8]== player :
        game_still_on1= False
        print(player + " Win")
    elif board[2]== board[4] and board[4]== player and  board[4]== board[6]:
        game_still_on1= False
        print(player+ " Win")
    else:
        check_if_tie(player)

    return game_still_on1

def check_if_tie(player):
    game_still_on1 = True
    count = 0
    for i in range(0,len(board)):
        if board[i] == "X" or board[i] == "O":
            count += 1
    if count == len(board):
        print("Tie")
        game_still_on1 = False
    return game_still_on1

def flip_player():
    return

play_game()





