i = 0
register = 0
for x in range(156):
    if i == 15:
        i = 0
    if i == 0:
        Q2 = 0
        Q3 = 0
    else:
        Q2 = (i & 4) >> 2
        Q3 = (i & 8) >> 3

    schaeffer_stroke = Q2 & Q3
    if schaeffer_stroke == 0:
        schaeffer_stroke = 1
    else:
        schaeffer_stroke = 0
    if register == 0:
        sum3 = 0
        sum5 = 0
    else:
        sum3 = (register & 4) >> 2
        sum5 = (register & 16) >> 4
    adder = sum3 ^ sum5 ^ schaeffer_stroke
    register = (register << 1) | adder
    register = register & 255

    register_str = format(register, 'b')
    print(x + 1, ' ', register_str.rjust(8, '0'))
    if x == 27 or x == 155:
        print('Шестанадцатиричный код: ', format(register, 'x'), 'такт: ', x + 1)
    i += 1