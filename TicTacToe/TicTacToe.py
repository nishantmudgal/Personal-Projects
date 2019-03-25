board = [" " for i in range(10)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    print(row1, row2, row3, sep = "\n", end = "\n")

def players_turn(icon):
    turn_choice = int(input("Enter your move(1-9)").strip())
    if board[turn_choice - 1] == " ":
        board[turn_choice-1] = icon
    else:
        print("Occupied, Please choose another one...")
        players_turn(icon)

def is_victory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[6] == icon and board[4] == icon and board[2] == icon):
      return True
    else:
      return False

def is_draw():
    if " " not in board:
        return True
    return False

while True:
    #player 1 -> 'X'
    players_turn('X')
    if is_victory('X'):
        print("Congratulations 'X', You Win!!!!")
        break

    print_board()

    if is_draw():
        print("Draw,  Well Played!!")
        break


    #player 2 -> 'O'
    players_turn('O')
    if is_victory('O'):
        print("Congratulations 'O', You Win!!!!")
        break

    print_board()

    if is_draw():
        print("Draw,  Well Played!!")
        break
