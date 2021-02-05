from utilities import *
b = colors()
clear()

num = testInt( '[int] Digite até que número você quer ver: ')
seq = fibonacci(num)

for (k,v) in enumerate(seq):
    if k == 0 and len(seq) != 1:
        print( f'{b[2][2]}[{v}]', end='')
    elif len(seq) == 1:
        print( f'{b[2][2]}[0]{b[2][3]} {k+1}ª número da lista.{b[0]}')
    elif k == len(seq) -1:
        print( f' > {b[2][3]}[{v}]{b[0]}')
    else:
        print( f' > [{v}]', end='')
print()
