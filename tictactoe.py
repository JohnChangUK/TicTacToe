import os
import time
import random

board = ["", " ", " ", " ", " ", " ", " ", " ", " ", " ",]

def print_board():
    print "   |   |   "
    print " "+board[1]+" | "+board[2]+" | "+board[3]+" "
    print "   |   |   "
    print "---|---|---"
    print "   |   |   "
    print " "+board[4]+" | "+board[5]+" | "+board[6]+" "
    print "   |   |   "
    print "---|---|---"
    print "   |   |   "
    print " "+board[7]+" | "+board[8]+" | "+board[9]+" "
    print "   |   |   "

def is_x_winner(board):
    if (board[1] == "X" and board[2] == "X" and board[3] == "X") or \
        (board[4] == "X" and board[5] == "X" and board[6] == "X") or \
        (board[7] == "X" and board[8] == "X" and board[9] == "X") or \
        (board[1] == "X" and board[4] == "X" and board[7] == "X") or \
        (board[2] == "X" and board[5] == "X" and board[8] == "X") or \
        (board[3] == "X" and board[6] == "X" and board[9] == "X") or \
        (board[1] == "X" and board[5] == "X" and board[9] == "X") or \
        (board[3] == "X" and board[5] == "X" and board[7] == "X"):
        return True
    else:
        return False

def is_o_winner(board):
    if (board[1] == "O" and board[2] == "O" and board[3] == "O") or \
        (board[4] == "O" and board[5] == "O" and board[6] == "O") or \
        (board[7] == "O" and board[8] == "O" and board[9] == "O") or \
        (board[1] == "O" and board[4] == "O" and board[7] == "O") or \
        (board[2] == "O" and board[5] == "O" and board[8] == "O") or \
        (board[3] == "O" and board[6] == "O" and board[9] == "O") or \
        (board[1] == "O" and board[5] == "O" and board[9] == "O") or \
        (board[3] == "O" and board[5] == "O" and board[7] == "O"):
        return True
    else:
        return False


while True:
    os.system("Clear")
    print_board()

    # Get player X input
    choice = raw_input("Please choose an empty space for X. ")
    choice = int(choice)

    # Check to see if the space is empty first
    if board[choice] == " ":
        board[choice] = "X"
    else:
        print "Sorry, that space is taken!"
        time.sleep(1)

    # Check for X win
    if is_x_winner(board):
        os.system("Clear")
        print_board()
        print "X Wins! Congrats!"
        break

    os.system("Clear")
    print_board()

    # Check for a Tie (Board full with no Winning Matches)
    isFull = True
    if " " in board:
        isFull = False

    # If board is full, display Message
    if isFull:
        print "It's a Tie!"
        break

    # Get player O input
    choice = raw_input("Please choose an empty space for O. ")
    choice = int(choice)

    # Check to see if the space is empty first
    if board[choice] == " ":
        board[choice] = "O"
    else:
        print "Sorry, that space is taken!"
        time.sleep(1)

    # Check for O win
    if is_o_winner(board):
        os.system("Clear")
        print_board()
        print "O Wins! Congrats!"
        break

    # Check for a Tie (Board full with no Winning Matches)
    isFull = True
    if " " in board:
        isFull = False

    # If board is full, display Message
    if isFull:
        print "It's a Tie!"
        break

