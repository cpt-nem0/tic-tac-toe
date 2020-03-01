def playerInput():
    while True:
        player = input(' Player1 select from "X" or "O" to play: ').upper()
        if player == 'X' or player == 'O':
            break
    if player == 'X':
        player1 = 'X'
        player2 = 'O'
        print('\n Player2 you have given: "O".\n')
    else:
        player1 = 'O'
        player2 = 'X'
        print('\n Player2 you have given: "X".\n')

    return player1, player2


def printBoard():
    print(
        f'''
        {theBoard['top-L']}|{theBoard['top-M']}|{theBoard['top-R']}
        -+-+-
        {theBoard['mid-L']}|{theBoard['mid-M']}|{theBoard['mid-R']}
        -+-+-
        {theBoard['low-L']}|{theBoard['low-M']}|{theBoard['low-R']}
        '''
    )


def boardStructure():       # structure 'coz of keypad layout
    print("""
    Board Structure:
        (7)|(8)|(9)
        ---+---+---
        (4)|(5)|(6)
        ---+---+---
        (1)|(2)|(3)
    """)


def checkPosition(position):
    if theBoard[position] == 'X' or theBoard[position] == 'O':
        return True
    else:
        return False


def checkWin():
    pass


boardStructure()    # board structure for instructions
player1, player2 = playerInput()
print("\n LET'S BEGIN!! \n")

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
indexes = {7: 'top-L', 8: 'top-M', 9: 'top-R',
           4: 'mid-L', 5: 'mid-M', 6: 'mid-R',
           1: 'low-L', 2: 'low-M', 3: 'low-R'}

turn = player1
i = 0
while i < 9:
    print(f'Player "{turn}" turn, enter your position: ')
    pos = int(input('> '))
    while True:
        if pos > 1 or pos < 9:
            try:
                if not checkPosition(indexes[pos]):
                    theBoard[indexes[pos]] = turn
                    if turn == player1:
                        turn = player2
                    else:
                        turn = player1
                    printBoard()
                    i += 1
                    break
                else:
                    print('\n Position not Empty.\n')
                    break
            except KeyError:
                print('\n Pos must be between 1-9. \n')
                break
print('\n GAME HAS ENDED!!')
