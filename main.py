# Essas duas linhas apenas limpam o terminal/cmd antes de executar o código própriamente dito...
from os import system, name
system( 'clear' if name == 'posix' else 'cls')





### Primeiramente, vamos deixar que o própio usuário digita quantos números ele quer ver da sequência. ###
num = input( '[int] Digite até que número você quer ver: ')
while True:
    try:
        num = int(num)
    except ValueError:
        num = input( '\033[31m[int] Digite até que número você quer ver:\033[m ')
    else:
        break
print()

### Segue as variáveis que vamos usar. ###
past = 0
present = 1
future = past + present

### Agora a lógica para mostrar na tela. ###
for c in range( 0, num):
    if c == 0:
        print( f'\033[32m[{past}]', end='')
    else:
        print( f' > [{past}]', end='')
    past = present
    present = future
    future = past + present
print( '\n\033[m')
## Descrição: Esse bloco sempre mostra o "passado", depois ele (presta atenção) torna o "passado" "presente", o "presente" "futuro", e o "futuro" a soma entre o "passado" e o "presente".
# Se o contador estiver no primeiro valor, ele vai mostrar a menságem de abertura, a ultima linha muda a cor do terminal para o normal e pula uma linha para deixar o código mais organizado...