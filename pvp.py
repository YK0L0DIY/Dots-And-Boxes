#
# developed by y.kolodiy
# 02-0-72019
#

"""
player vs player mode
"""
import table

def start(x, y):
    """
    beginning of the game
    :param x: rows
    :param y: columns
    """
    t = table.create_tab(x, y)
    play(t)


def validate(tab, play):
    """
    validades the players input
    :param tab: table
    :param play: players input
    :return: validation
    """
    cord1, cord2 = play
    x, y = cord1
    j, v = cord2

    try:
        x = x * 2
        y = y * 2
        j = j * 2
        v = v * 2
    except:
        return False

    distX = x - j
    distY = y - v

    cordX = (x + j) / 2
    cordY = (y + v) / 2

    try:
        if tab[x][y] == '+' and tab[j][v] == '+':
            if distX == 2 or distX == -2 or distX == 0:
                if distY == 2 or distY == -2 or distY == 0:
                    if tab[int(cordX)][int(cordY)] == 1 or tab[int(cordX)][int(cordY)] == '1':
                        return True
                    return False
                else:
                    return False
            else:
                return False
        else:
            return False
    except:
        return False


def changePlayer(player):
    """
    chnage the player
    :param player: player that is playing
    :return: next player
    """
    if player == "A":
        return "B"
    return "A"


def gameInput():
    """
    make the imput of the play
    :return: the input
    """
    try:
        x, y = eval(input('Your play (x,y),(j,v)'))

    except:
        print("Error in the input")

    return x, y


def atualizeTab(tab, play):
    """
    atualization of the table
    :param tab: table
    :param play: the play
    :return: new table atualizated
    """
    cord1, cord2 = play
    x, y = cord1
    j, v = cord2

    x = x * 2
    y = y * 2
    j = j * 2
    v = v * 2

    cordX = (x + j) / 2
    cordY = (y + v) / 2

    if cordY % 2 != 0:
        tab[int(cordX)][int(cordY)] = "-"
    else:
        tab[int(cordX)][int(cordY)] = "|"

    return tab


def gameEnd(tab):
    """
    confirm if are any posibole plays
    :param tab: table
    :return: true if is possibol to play
    """
    for x in tab:
        for y in x:
            if y == 1 or y == '1':
                return False
    return True


def sqware(tab, player):
    """
    creates the sqwares if the exists
    :param tab: table
    :param player: atual player
    :return: modified table
    """
    hit = False
    for x in range(0, len(tab), 2):
        for y in range(0, len(tab[x]), 2):
            try:

                if tab[x][y + 1] != 1 \
                        and tab[x + 1][y] != 1 \
                        and tab[x + 1][y + 2] != 1 \
                        and tab[x + 2][y + 1] != 1 \
                        and tab[x][y + 1] != '1' \
                        and tab[x + 1][y] != '1' \
                        and tab[x + 1][y + 2] != '1' \
                        and tab[x + 2][y + 1] != '1':
                    if tab[x + 1][y + 1] == " ":
                        tab[x + 1][y + 1] = player
                        hit = True
            except:
                pass

    return tab, hit


def points(tab):
    """
    return the points of each player
    :param tab: table
    :return: points tuple
    """
    pointsA = 0
    pointsB = 0

    for x in tab:
        for y in x:
            if y == "A":
                pointsA = pointsA + 1
            elif y == "B":
                pointsB = pointsB + 1

    return pointsA, pointsB


def resume():
    """
    resumes the existed game in fali save
    """
    saved = open('save', 'r')
    tab = []
    maxX = int(saved.readline())
    maxY = int(saved.readline())

    for x in range(0, maxX, 1):
        line = saved.readline().rstrip('\n')
        col = list(line)
        col = col[:maxY]
        tab.append(col)

    player = saved.readline()
    play(tab, player)


def saveGame(tab, player):
    """
    saves the atual game in file "save"
    :param tab: table
    :param player: atual player
    :return: just back
    """
    save = open('save', 'r+')
    save.truncate(0)
    save.writelines(str(len(tab)) + '\n')
    save.writelines(str(len(tab[0])) + '\n')

    for x in tab:
        for y in x:
            save.writelines(str(y))
        save.writelines("\n")

    save.writelines(player)
    save.close()
    print("Game saved!")
    return


def play(tab, player="A"):
    """
    simple play
    :param tab: table
    :param player: player to play
    :return: back
    """
    table.print_tab(tab)

    print("player ", player, ":")

    print("0 - save game\n1 - Insert Play")

    while 1:
        try:
            op = int(input())

            if op == 0 or op == 1:
                break
            else:
                print("Invalid Option")
        except:
            print("Invalid Option")

    if op == 0:
        saveGame(tab, player)
    elif op == 1:

        while 1:
            tryPlay = gameInput()
            if validate(tab, tryPlay):
                break
            print("Jogda invalida")

        tab = atualizeTab(tab, tryPlay)
        tab, hit = sqware(tab, player)

        if hit:
            play(tab, player)

        if gameEnd(tab):
            a, b = points(tab)
            table.print_tabuleiro(tab)
            print("Game ended. Score is; A-", a, " and B-", b)

            return

        play(tab, changePlayer(player))

    play(tab, player)


if __name__ == "__main__":
    start(5, 7)
