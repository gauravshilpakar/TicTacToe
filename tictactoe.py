print('TicTacToe\n')

# board= []
# for i in range(1,10,1):
#     board.append('')

board = ['O','O','X','5','O','O','X','O','X']

def display_board(board):
    print('\n')
    print(board[0]+'|'+board[1]+'|'+board[2])
    print(board[3]+'|'+board[4]+'|'+board[5])
    print(board[6]+'|'+board[7]+'|'+board[8])
    
def player_input():
    p1=''
    while p1!='x' and p1!='o':
        p1 = input('\nPlayer 1 select "x" or "o". ').lower()
    if p1=='x':
        p2='o'
    else:
        p2='x'
        
    print(p1,p2)  
    
def place_marker(board, marker, position):
    board[position-1]=marker

def win_check(board, mark):
    
    first= board.index(mark)
    
    if first == 0 or first==3 or first ==6:
        if board[first]== board[first+1]== board[first+2]==mark:
            print(f'{first} horizontal.')
            print(f'{mark} is winner.') 
    if first == 0 or first==1 or first ==2:
        if board[first]== board[first+3]== board[first+6]==mark:
            print(f'{first} vertical.')
            print(f'{mark} is winner.')
    if first == 0:
        if board[first]== board[first+4]==board[first+8]==mark:
            print(f'{first} first diagonal.')
            print(f'{mark} is winner.')
    if first == 2:
        if board[first]== board[first+2]==board[first+4]==mark:
            print(f'{first} second diagonal.')
            print(f'{mark} is winner.') 

def space_check(board, position):
    x= board[position-1]
    print(f'In board position {position} there is {x}')
    if (board[position-1]=='X' or board[position-1]=='O'):
        print('\nPosition is filled.')
        return False
    elif board[position-1]==str(position):
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

        
display_board(board)
# player_input()
display_board(board)
win_check(board,'X')
print(space_check(board, 5))
print(full_board_check(board))

# while True:
#     pos=''    
#     while pos in str([1,2,3,4,5,6,7,8,9]):
#         pos= input('Select position for your move. ')

#     place_marker(board, )

