import logger as log

def check_float_number(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Некорректный ввод. Повторите попытку")
            log.log_error('Некорректный ввод float')
    return number

def check_complex_number(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = complex(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Некорректный ввод. Повторите попытку")
            log.log_error('Некорректный ввод complex')
    return number

def check_regime(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            if number in [0, 1, 2]:
                is_OK = True
            else:
                print("Некорректный ввод. 0 - закрыть программу; 1 - float; 2 - complex")
                log.log_error('Некорректный ввод режима работы (некорректная цифра)')
        except ValueError:
            print("Некорректный ввод. Повторите попытку")
            log.log_error('Некорректный ввод режима работы (введена не цифра)')
    return number

def check_operation(inputText):
    operation_list = ['+', '-', '*', '/']
    is_OK = False
    while not is_OK:
        operation = input(f'{inputText}')
        if operation in operation_list:
            is_OK = True
            return operation
        else:
            print('Выберите верную операцию')
            log.log_error('Некорректный ввод операции')