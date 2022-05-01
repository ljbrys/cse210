"""
Larry J> Brys
CSE 210
WK 2 
Tic-Tac-Toe Game
"""

def main():
    #print ("program has started")
    board = []
    whos_turn = "x"

    board = make_board()

    is_no_winner = True
    while (is_no_winner):
        #print ("program is working")
        print_board(board)
        make_move(board,whos_turn)
        print()
        print()
        
        if (whos_turn == "x"):
            whos_turn = 'o'
        else:
            whos_turn = 'x'
        
        is_no_winner = is_game_won(board)
        draw = is_game_draw
        if (draw):
            is_no_winner = False

    print(f"Good game. Thanks for playing")










def is_game_draw (board):
    for number in range(9):
        if board[number] != "x" and board[number] != "o":
            return False
    return True


def make_board():
    temp_board = []
    for number in range (9):
        temp_board.append(number +1)
    return temp_board

def make_move(board,whos_turn):
    everything_good = True
    number = 0
    while (everything_good):
        number=int(input(f"{whos_turn} turn to choose a square (1-9): "))
        #print("made it to if")
        if (board[number-1] == 'x' or board[number-1] == 'o'):
            print(f"I am sorry but that square is not available")
        else:
            everything_good = False
           # print("made it to else")
    #print(number)
    board[number-1] = whos_turn

def is_game_won(board):
    there_is_not_winner = True
    if(board[0]==board[1]==board[2] or
    board[3]==board[4]==board[5] or  
    board[6]==board[7]==board[8] or
    board[0]==board[3]==board[6] or
    board[1]==board[4]==board[7] or
    board[2]==board[5]==board[8] or
    board[0]==board[4]==board[8] or
    board[6]==board[4]==board[2]):
        there_is_not_winner = False
    return there_is_not_winner

def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]} ")
    print("-+-+-+-+-+-+")
    print(f"{board[3]} | {board[4]} | {board[5]} ")
    print("-+-+-+-+-+-+")
    print(f"{board[6]} | {board[7]} | {board[8]} ")
 






# Call main to start this program.
if __name__ == "__main__":
    main()