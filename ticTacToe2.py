# Tic Tac Toe game V2
# Work in progress

# Import modules
import os, re, sys

# Define the board, with all blank values
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

# Default turn
turn = 'X'

# List of current choices, all are available at beginning
# These are not pulled from the dictionary, because they are not sorted that way
# choices = list(theBoard.keys()) # to pull from dictionary
choices = ['top-L', 'top-M', 'top-R',
           'mid-L', 'mid-M', 'mid-R',
           'low-L', 'low-M', 'low-R']
           
ex = re.compile(r'^(top|mid|low)-(l|m|r)$', re.IGNORECASE)

def printBoard(board):
    print('-------------')
    print('|   |   |   |')
    print('| %s | %s | %s |' % (board['top-L'], board['top-M'], board['top-R']))
    print('|   |   |   |')
    print('-------------')
    print('|   |   |   |')
    print('| %s | %s | %s |' % (board['mid-L'], board['mid-M'], board['mid-R']))
    print('|   |   |   |')
    print('-------------')
    print('|   |   |   |')
    print('| %s | %s | %s |' % (board['low-L'], board['low-M'], board['low-R']))
    print('|   |   |   |')
    print('-------------')
 
def validateMove(pMove):
    val = ex.search(pMove)
    
    if not val:
        return False
    else:
        return True
    

for i in range(9):
    os.system('clear')
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    print('Your choices are: ', end='')
    print(', '.join(choices))
    
    while True:
        print('Input: ', end='')
        move = input()
        
        if move == 'quit' or move == 'exit':
            print('Bye!')
            sys.exit()
        
        elif move == 'win':
            break
        
        elif validateMove(move) == False:
            print('Incorrect move format')
            
        else:
            moveFirst = move[:3] # formats case of characters
            moveLast = move[4]
            moveComplete = moveFirst.lower() + '-' + moveLast.upper()
            
            if moveComplete not in choices: # detects whether valid move
                print('That move is not valid - use one from the current choices')
            else:
                theBoard[moveComplete] = turn
                choices.remove(moveComplete)
                if turn == 'X': 
                    turn = 'O'
                else:
                    turn = 'X'
                break
                
    if move == 'win':
        break
    
# TODO: add function to determine winner if there is one

os.system('clear')
print('Here is the final board:')
printBoard(theBoard)
print('You will have to determine the winner, if there is one') # no victory check yet
