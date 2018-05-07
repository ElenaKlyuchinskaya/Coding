h = int(input('height: '))


def pyramida(h):
    if h < 1:
        print('height can not be small')
    elif h > 23:
        print('too big height ')
    elif h - int(h) != 0:
        print('enter an integer')
    else:
        a = [[' '] * (h + 1) for i in range(h)]
        for i in range(h):
            for j in range(h + 1):
                if i <= j:
                    a [i][j] = '#'
                elif i > j:
                    a [i][j] = ' '
        for row in a.__reversed__():
            print(' '.join([str(elem) for elem in row]))


print(pyramida(h))