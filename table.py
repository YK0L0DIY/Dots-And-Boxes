#
# developed by y.kolodiy
# 02-0-72019
#

def create_tab(rows, coluns):
    """
    generates a table of rows*columns
    :param rows: the number of rows for the table
    :param coluns: the number of columns fot the table
    :return:
    """
    tab = []
    for x in range(rows):
        col = []

        for i in range(coluns):
            col.append('+')

            if i == coluns - 1:
                pass
            else:
                col.append(1)

        tab.append(col)

        col = []

        if x == rows - 1:
            return tab

        for i in range(coluns):
            if i == 0:
                col.append(1)
            elif int(i) % 2 == 0:
                col.append(1)
            else:
                col.append(1)

            if i == coluns - 1:
                pass
            else:
                col.append(' ')

        tab.append(col)

    return tab


def print_tab(t):
    """
    prints the table received
    :param t: the table
    """
    print(' ', end=' ')
    for x in range(len(t[0])):
        if x % 2 != 0:
            print(' ', end=' ')
        else:
            print(x // 2, end=' ')
    print()

    cont = 0

    for line in t:
        if cont % 2 != 0:
            print(' ', end=' ')
        else:
            print(cont // 2, end=' ')

        for colun in line:
            if colun == 1 or colun == '1':
                print(' ', end=' ')
            else:
                print(colun, end=' ')
        print()
        cont = cont + 1

if __name__ == "__main__":
    t = create_tab(7, 3)
    print_tab(t)
