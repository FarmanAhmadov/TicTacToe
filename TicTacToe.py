#!/usr/bin/env python
# coding: utf-8

# ## TicTacToe

# In[ ]:


# Global Variables
game_is_going = True

current_player = "X"

# board

winner = None


board = ["-","-","-",
        "-","-","-",
        "-","-","-"]

def display():

  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():

  # Displaying initial board
  display()

  while game_is_going:

    handle_turn(current_player)

    check_game_over()

    flip_player()



  if winner == "X" or winner == "O":

    print(winner + " won.")

  else: print("Tie")

  
def handle_turn(player):

  print(player + "\'s turn")

  

  position = input("Enter the position 1-9: ")

  while position not in ["1","2","3","4","5","6","7","8","9"]:
    position = input("Enter the position 1-9: ")
    
  position = int(position)

  board[position] = player

  display()

def check_game_over():

  

  check_for_winner()

  check_tie()

def check_for_winner():
  #check rows/ columns/ diagonals

  global winner

  row_winner = check_rows()

  column_winner = check_columns()

  diagonal_winner = check_diagonal()

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

  global game_is_going

  row1 = board[0] == board[1] == board[2] != "-"
  row2 = board[3] == board[4] == board[5] != "-"
  row3 = board[6] == board[7] == board[8] != "-"

  if row1 or row2 or row3:
    game_is_going = False
  
  if row1:
    return board[0]
  elif row2:
    return board[3]
  elif row3:
    return board[7]

def check_columns():
  global game_is_going

  column1 = board[0] == board[3] == board[6] != "-"
  column2 = board[1] == board[4] == board[7] != "-"
  column3 = board[2] == board[5] == board[8] != "-"

  if column1 or column2 or column3:
    game_is_going = False
  
  if column1:
    return board[0]
  elif column2:
    return board[1]
  elif column3:
    return board[2]
  

def check_diagonal():
  global game_is_going

  diagonal1 = board[0] == board[4] == board[8] != "-"
  diagonal2 = board[2] == board[4] == board[6] != "-"
  

  if diagonal1 or diagonal2 :
    game_is_going = False
  
  if diagonal1:
    return board[0]
  elif diagonal2:
    return board[2]
  






def check_tie():
  global game_is_going

  if "-" not in board:
    game_is_going = False

  

def flip_player():

  global current_player

  if current_player == "X":

    current_player = "O"
  elif current_player == "O":

    current_player = "X"
  
  


play_game()









# display board
#play game
#check Win
 #check columns/rows/diagonal
#check Tie
# Flip player


# In[ ]:




