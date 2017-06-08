import os
import time
import random

board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ",]

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

while True:
    os.system("Clear")
    print_board()

    choice = raw_input("Please choose an empty space for X. ")
    choice = int(choice)

    # Check to see if the space is empty first
    if board[choice] == " ":
        board[choice] = "X"
    else:
        print "Sorry, that space is taken!"
        time.sleep(1)

    # Check for X win
    if (board[1] == "X" and board[2] == "X" and board[3] == "X"):
        print "X Wins! Congrats!"
        break
        