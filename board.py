import random

# Game board
board = [0, 1, 2,
        3, 4, 5,
        6, 7, 8]

def show():
    print board[0], '|',board[1], '|', board[2]
    print '----------'
    print board[3], '|',board[4], '|', board[5]
    print '----------'
    print board[6], '|',board[7], '|', board[8]

while True:

    input= raw_input("Select a Spot: ")
    input = int(input)

    if board[input] != 'x' and board[input] != 'o':
        board[input] = 'x'

        finding = True

        while finding:
            random.seed() # Gives a random number, random generator
            opponent = random.randint(0, 8)

            if board[opponent] != 'o' and board[opponent] != 'x':
                board[opponent] = 'o'
                finding = False

    else:
        print ("This spot is taken!")

    show()

