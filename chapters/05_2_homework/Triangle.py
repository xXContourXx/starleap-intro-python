def is_triangle(a, b, c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        print('Yes, it is a triangle')
    else:
        print('No, it is not a triangle')

    a = float(input('enter the lenght of a'))
    b = float(input('enter the lenght of b'))
    c = float(input('enter the lenght of c'))

    is_triangle(a, b,c)