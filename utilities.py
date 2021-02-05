def clear():
    '''Limpa a tela (No windows e no Linux/Mac).'''
    from os import system, name
    if name == 'posix':
        system( 'clear')
    else:
        system( 'cls')

def colors():
    '''Retorna uma lista com os códigos de cores do padrão ANSI da UniCode...'''
    return [
        '\033[m', [
            '\033[0m', '\033[1m', '\033[2m', '\033[3m', '\033[4m', '\033[5m', '\033[6m', '\033[7m'
        ], [
            '\033[30m', '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m' 
        ], [
            '\033[40m', '\033[41m', '\033[42m', '\033[43m', '\033[44m', '\033[45m', '\033[46m', '\033[47m' 
        ]
    ]

def testInt(msg):
    '''Insiste que o usuário digite um valor inteiro. "msg"' serve como a menságem de input do terminal.'''
    number = input(msg)
    while True:
        try:
            number = int(number)
        except:
            number = input( colors()[2][1] + msg + colors()[0])
        else:
            break
    return number

def fibonacci( num = 10):
    '''Retorna uma llista numérica na sequência de Fibonacci, sendo "num" o tamanho da lista (o valor padrão é 10).'''
    seq = [ 0, 1, 1]
    if num < 4:
        return seq[0:num]
    else:
        for c in range(3, num):
            seq.append( seq[ c -1] + seq[ c -2])
        return seq