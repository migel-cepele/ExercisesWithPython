#loja x-rrethor
#kete loje do e krijojme jo ne menyre vizuale por sa per te mesuar pak kodimin
#si fillim do krijojme nje fushe me ane te nje grid system

#per te krijuar kete grid do perdorim nje vektor te emertuar board
from multiprocessing.connection import answer_challenge


board = [' ' for x in range(10)]; #jane perdorur 10 vlera ne menyre qe useri te vendosi 1-9 dhe jo 0-8

def insertletter(letter, pos): #vendos letter ne pozicionin e duhur ne tabele
    board[pos] = letter

def spaceFree(pos):
    return board[pos] == ' ' #percakton nese vendi ne tabele eshte bosh apo jo

def printBoard(board):
    print(' | ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('----------------')
    print(' | ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------------')
    print(' | ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------------'); #fun qe printon fushen

def isWinner(bo, le):
    return((bo[1] == le and bo[2]==le and bo[3]==le) or 
    (bo[4]==le and bo[5]==le and bo[6]==le) or 
    (bo[7]==le and bo[8]==le and bo[9]==le) or
    (bo[1]==le and bo[5]==le and bo[9]==le) or
    (bo[3]==le and bo[5]==le and bo[7]==le) or
    (bo[1]==le and bo[4]==le and bo[7]==le) or
    (bo[2]==le and bo[5]==le and bo[8]==le) or
    (bo[3]==le and bo[6]==le and bo[9]==le));
    
def isBoardFull(board):
    x = len(board)
    if (x > 1):
        return False
    else:
        return True

def playerMove():
    kot = True
    while kot:
        try:

            p = input('Vendosni nje numer nga 1 deri ne 9: ');
            p = int(p)
            if (p > 0 and p < 10):

                if (spaceFree(p) == True):
                    kot = False
                    insertletter('X', p)
                else:
                    print('Hapsira eshte e zene')
            else:
                print('Pozicioni i pavlefshem')
        except:
            print('Vendosni nje numer')

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]            

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0];#krijon nje liste me gjithe levizjet e mundshme
    move = 0

    for let in ['X', 'O']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    #if corners open
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    #nese qendra eshte bosh
    if 5 in possibleMoves:
        move = 5
        return move 

    #nese anesoret jane bosh 
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def main():#ketu kryhen veprimet ne lidhje me lojen
    print('Miresevini ne lojen x-o. Per te luajtur duhet te vendosni nje nr nga 1-9 per pozicionin ne cilin doni te vendosni x duke filluar nga top-left.')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('o wins')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('game is a tie')
            else:
                insertletter('O', move)
                print('kompjuteri vendosi O ne poz: ', move)
                printBoard(board)
        else:
            print('x wins')
            break

    if isBoardFull(board):
        print('barazim')


while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        break                    










