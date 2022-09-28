import check  as ch

def const():
    ver = ch.check_regime('\nВведите режим работы программы:\n0 - закрыть программу;\n1 - float;\n2 - complex;\nВвод ')
    if ver == 1:
        a = ch.check_float_number('Введите первое число ')
        b = ch.check_float_number('Введите второе число ')
    elif ver == 2:
        a = ch.check_complex_number('Введите первое число ')
        b = ch.check_complex_number('Введите второе число ')
    elif ver == 0:
        a = 0
        b = 0
    return a, b, ver

def oper():
    operation = ch.check_operation('Выберите операцию на числами из списка: "*", "/", "+", "-"\nВвод  ')
    return operation