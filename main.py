#
# developed by y.kolodiy
# 02-0-72019
#

import sys, pvp

def start():
    """
    begin the game
    """
    textInicial = [
        '0 - Exit',
        '1 - Player vs Player',
        '2 - Resume Game'
    ]

    while (1):

        for x in range(len(textInicial)):
            print(textInicial[x])

        try:
            op = int(input())

            if (op >= len(textInicial) or op < 0):
                print("Invalid Option")
            else:
                break
        except:
            print("Invalid Option")

    if op == 0:
        sys.exit()

    elif op == 1:
        try:
            (x, y) = eval(input('Grid dimension? (lines, columns)\n'))
        except:
            print('Invalid input')

        pvp.start(x, y)

    elif op == 2:
        try:
            pvp.resume()
        except:
            print("Do not exist saved game")

    start()


if __name__ == "__main__":
    start()
