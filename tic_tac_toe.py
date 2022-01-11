'''
Assingment: Tic-Tac-Toe game.
Author: Christian Vargas
'''


print(" \u001b[42m\u001b[33;1m ********WELCOME TO TIC-TAC-TOE GAME******** \u001b[0m")
print()
player_1 = ("\u001b[35;1mX\u001b[0m")
player_2 = ("\u001b[34;1mO\u001b[0m")

def main():
    player = player_turn("")
    board = create_board()
    while not (has_winner(board) or draw(board)):
        display_board(board)
        make_move(player, board)
        player = player_turn(player)
        
    display_board(board)
    if draw(board) == True:
        print("Draw")
    elif player == player_1:
        print(f'Player "{player_2}" has win!!')
    elif player == player_2:
        print(f'Player "{player_1}" has win!!')
    keep_playing = input("Do you want to play again? (yes/no): ")
    if keep_playing == "yes":
        main()
    else:
        quit

def create_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board

def display_board(board):
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def draw(board):
    for square in range(9):
        if board[square] != player_1 and board[square] != player_2:
            return False
    return True

def has_winner(board):
    return(board[0] == board[1] == board[2] or
           board[3] == board[4] == board[5] or
           board[6] == board[7] == board[8] or
           board[0] == board[3] == board[6] or
           board[1] == board[4] == board[7] or
           board[2] == board[5] == board[8] or 
           board[0] == board[4] == board[8] or
           board[2] == board[4] == board[6])


def make_move(player, board):
    square = int(input(f"{player}'s turn to choose a square (1-9): "))
    board[square - 1] = player
    print()

def player_turn(current):
    if current =="" or current == player_2:
        return player_1
    elif current == player_1:
        return player_2

    

if __name__ == "__main__":
    main()