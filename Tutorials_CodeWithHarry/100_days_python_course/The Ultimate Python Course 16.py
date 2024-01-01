x = int(input('enter an integer: '))

match x:
    case 0:
        print('x is 0.')
    case 4:
        print('x is 4.')
    case _ if x != 0:
        print('x =', x)
        if x <0:
            print('x is a negative integer.')
        else:
            print('x is a positive interger.')
