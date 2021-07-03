import random

index = int(input("Digite o numero de participantes: "))
x = 0
array = []
while x <= (index -1):
    participante = str(input("Digite o nome do participante: "))
    array.append(participante)
    x += 1 

sorteia = str(input("Sortear agora? S/N"))
if (sorteia == "s"):
    print(random.choice(array))
