import os

os.system("clear")

class Board():
    def __init__(self):
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    def display(self):
        print (" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        print ("-----------")
        print (" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        print ("-----------")
        print (" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

    def update_cell(self, cell_no, player):
        self.cells[cell_no] = player

board = Board()
board.display()

def print_header():
    print("Play Tic Tac Toe! \n")

def refresh_screen():
    os.system("clear")

    print_header()

    board.display()

# while True acts an as Infinite loop
while True:
    refresh_screen()

    # Get X input
    x_choice = int(raw_input("\nX) Please choose 1 - 9. > "))

    # Updating Board
    board.update_cell(x_choice, "X")