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


def boardStructure():
    print("""
    Board Structure:
        (1)|(2)|(3)
        ---+---+---
        (4)|(5)|(6)
        ---+---+---
        (7)|(8)|(9)
    """)


def checkWin():
    pass


def intiBoard():
    theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
                'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
                'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


boardStructure()
player1 = input(' player1 select from "X" and "O" to play:')
player2 = input(' player2 select from "X" and "O" to play:')

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
indexes = {1: 'top-L', 2: 'top-M', 3: 'top-R',
           4: 'mid-L', 5: 'mid-M', 6: 'mid-R',
           7: 'low-L', 8: 'low-M', 9: 'low-R'}

turn1 = 1
turn2 = 0

for i in range(9):
    if turn1:
        while True:
            print(" Player 1 your turn, choose a position")
            pos = int(input('> '))
            if pos < 9 or pos > 1:
                theBoard[indexes[pos]] = player1
                turn1 = 0
                turn2 = 1
                printBoard()
                break
