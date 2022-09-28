import logger as log
import constants as con
import operations as  oper

def button_click():
    a, b, ver = con.const()

    if ver == 0:
        print('Программа отменена')
        log.log_exit()
        exit()

    operation = con.oper()

    if operation == '*':
        result = oper.mult(a, b)
    elif operation == '/':
        result = oper.div(a, b)
    elif operation == '+':
        result = oper.sum(a, b)
    elif operation == '-':
        result = oper.diff(a, b)

    print(f"{a} {operation} {b} = {result}")
    log.log_to_file(a, b, operation, result)
    button_click()