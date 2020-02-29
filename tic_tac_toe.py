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
player1 = input(' player1 select from "X" and "O" to play:').upper()
player2 = input(' player2 select from "X" and "O" to play:').upper()

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
indexes = {7: 'top-L', 8: 'top-M', 9: 'top-R',
           4: 'mid-L', 5: 'mid-M', 6: 'mid-R',
           1: 'low-L', 2: 'low-M', 3: 'low-R'}

turn = player1
for i in range(1, 9):
    while True:
        print(f'Turn of the player who has chosen "{turn}", enter your desired position: ')
        pos = int(input('> '))
        if pos > 1 or pos < 9:
            if not checkPosition(indexes[pos]):
                if turn == player1:
                    theBoard[indexes[pos]] = player1
                    turn = player2
                    printBoard()
                else:
                    theBoard[indexes[pos]] = player2
                    turn = player1
                    printBoard()
