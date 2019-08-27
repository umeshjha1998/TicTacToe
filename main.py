# board
# display board
# play game
# handle turn
# check win
  #check rows
  #check columns
  #check diagonals
#check tie
#flip player



#----- Global Variables -----


# Game Board
board = ["-","-","-",
        "-","-","-",
        "-","-","-",]

# If game still going
game_still_going = True


# Who won? or Tie?
winner = None

# Who's turn is it?
current_player = "X"

# Display Board
def display_board():
  print(board[0] + "|" + board[1] + "|" + board[2]      +"\t\t\t 1 | 2 | 3")
  print(board[3] + "|" + board[4] + "|" + board[5]      +"\t\t\t 4 | 5 | 6")
  print(board[6] + "|" + board[7] + "|" + board[8]      +"\t\t\t 7 | 8 | 9")


# Play a game of tic tac toe
def play_game():
  
  #display the initial board
  display_board()


  # while the game is still going
  while game_still_going:

    # handle a single turn of arbitrary player
    handle_turn(current_player)


    # CHECK IF THE GAME HAS ENDED
    check_if_game_over()

    # Flip to the other player
    flip_player()

# The game has ended
  if winner == "X" or winner == "O":
    print (winner + " won.")

  elif winner == None:
    print("It's a tie")


# Handle a single turn of an arbitrary player
def handle_turn(player):

  print(player + "'s turn")

  position = input("Choose a position from 1 to 9: ")
  
  valid = False
  while not valid:

    while position not in ["1","2","3","4","5","6","7","8","9"]:
      position = input("Invalid input. Enter valid input from 1-9: ")
    
    position = int(position) -1

    
    # Make sure spot is available in the round
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there again. ")

  board[position] = player
  display_board()


def check_if_game_over():
  check_for_winner()
  check_if_tie()


def check_for_winner():

  # Set up global variables
  global winner


  # check rows
  row_winner = check_rows()

  #chck columns
  column_winner = check_columns()

  #check diagonals
  diagonal_winner = check_diagonals()

  # Get the winner
  if row_winner:
    winner = row_winner

  elif column_winner:
    winner = column_winner

  elif diagonal_winner:
    winner = diagonal_winner

  else: 
    winner = None
  return 



def check_rows():

  # Set up global variables
  global game_still_going

  # check if any of the rows have same value ( and is not empty)
  row_1= board[0] == board[1] == board[2]  != "-"
  row_2= board[3] == board[4] == board[5]  != "-"
  row_3= board[6] == board[7] == board[8]  != "-"

  # If any row has a match flag that it's a win

  if row_1 or row_2 or row_3:
    game_still_going = False
  # Return the winner X or 0
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  return


def check_columns():
  # Set up global variables
  global game_still_going

  # check if any of the column have same value ( and is not empty)
  column_1= board[0] == board[3] == board[6]  != "-"
  column_2= board[1] == board[4] == board[7]  != "-"
  column_3= board[2] == board[5] == board[8]  != "-"

  # If any column has a match flag that it's a win

  if column_1 or column_2 or column_3:
    game_still_going = False
  # Return the winner X or O
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  return



def check_diagonals():
   # Set up global variables
  global game_still_going

  # check if any of the diagonal have same value ( and is not empty)
  diagonal_1= board[0] == board[4] == board[8]  != "-"
  diagonal_2= board[6] == board[4] == board[2]  != "-"

  # If any diagonal has a match flag that it's a win

  if diagonal_1 or diagonal_2 :
    game_still_going = False
  # Return the winner X or 0
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[6]

  return


def check_if_tie():
  # If there are no "-" in the matrix do a tie.
  global game_still_going
  if "-" not in board:
    game_still_going = False
  return


def flip_player():
  #global variables we need
  global current_player
  #if current player was X then change it to O
  if current_player ==  "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"

  return

play_game()
