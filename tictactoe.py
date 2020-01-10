import random
print('TicTacToe')

board= []
def board_setup(board):
    for i in range(1,10,1):
        board.append(str(i))

def display_board(board):
    print('\n')
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])
    
def player_input():
    p1=''
    while p1!='X' and p1!='O':
        p1 = input('\nPlayer 1 select "X" or "O". ').upper()
    if p1=='X':
        return ('X', 'O')
    else:
        return ('O', 'X')
        
    print(f"Player1= {p1}\nPlayer2= {p2}")  
    
def place_marker(board, marker, position):
    board[position-1]=marker

def win_check(board, mark):
    p= board.index(mark)
    
    if p == 0 or p==3 or p ==6:
        if board[p]== board[p+1]== board[p+2]==mark:
            print(f'{mark} is winner.') 
            return True
    if p == 0 or p==1 or p ==2:
        if board[p]== board[p+3]== board[p+6]==mark:
            print(f'{mark} is winner.')
            return True
    if p == 0:
        if board[p]== board[p+4]==board[p+8]==mark:
            print(f'{mark} is winner.')
            return True
    if p == 2:
        if board[p]== board[p+2]==board[p+4]==mark:
            print(f'{mark} is winner.') 
            return True

def space_check(board, position):
    x= board[position-1]
    #print(f'In board position {position} there is "{x}"')
    if (board[position-1]=='X' or board[position-1]=='O'):
        print('\nPosition is filled.')
        return False
    elif board[position-1]==str(position):
        print('\nMove Complete')
        return True   

def full_board_check(board):
    count=0
    for i in range(len(board)):
        if (board[i]=='X' or board[i]=='O'):
            count+=1
            
    if count==9:
        print('\nBoard Full')
        return True
    else:
        print('\nBoard Has Empty Space')
        return False
    
def player_choice(board, marker):
    trial = True
    while trial:
        choice=''
        while choice not in ['1','2','3','4','5','6','7','8','9']:
            choice = (input('Enter the position for your move... [1-9]: '))
        choice = int(choice)
        if space_check(board,choice):
            break    
    place_marker(board, marker, choice)
    display_board(board)
       
board_setup(board)        
display_board(board)
p1,p2=player_input()               

while True:  
    print(f'Player 1 {p1} Turn')
    player_choice(board,p1)
    if win_check(board,p1):
        break
    
    print(f'Player 2 {p2} Turn')
    player_choice(board,p2)
    if win_check(board,p2):
        break