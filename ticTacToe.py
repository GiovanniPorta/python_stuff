# Tic Tac Toe game
# Work in progress

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

turn = 'X'
# choices = list(theBoard.keys()) # these are not sorted
choices = ['top-L', 'top-M', 'top-R',
           'mid-L', 'mid-M', 'mid-R',
           'low-L', 'low-M', 'low-R']

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R']) 
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    #print('Your choices are: ' + str(choices))
    print('Your choices are: ', end='')

    print(', '.join(choices)) # prints choices - new method

    #for c in choices:
    #    print(c + ' ', end='') # prints choices - old method
    #    
    #print('')
    
    while True:
        move = input()

        # add if statement so don't have to act upon IndexError?
        # if len(move) < 5
        # to-do: make validity check a function that returns true or false
        
        try:
            moveFirst = move[:3] # formats case of characters
            moveLast = move[4]
            moveComplete = moveFirst.lower() + '-' + moveLast.upper()
            
            if moveComplete not in choices: # detects whether valid move
                print('That is not a valid move')

            else: # if a valid move: changes key, updates turn
                theBoard[moveComplete] = turn
                if turn == 'X': 
                    turn = 'O'
                else:
                    turn = 'X'
                break
        except IndexError: # if string indexing fails
            print('That is not a valid move')

    for x in choices: # removes choice(s) no longer valid
        if theBoard[x] != ' ':
            choices.remove(x)
        else:
            continue

print('Someone won the game, that is for you to figure out!') # no victory check yet
print('Here is the final board:')
printBoard(theBoard)

print('this is the case')
