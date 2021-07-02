tabuada = int(input('Digite um numero para saber sua tabuada: '))
index = 1

print('='*14)
while index <= 10:
    print('{:2} + {:2} = {:2}'.format(tabuada, index, tabuada+index))
    index += 1
print('='*14)