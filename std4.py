print('Vanos calcular o seu IMC? (Indice de Massa Corporal)')
altura = float(input('Informe sua altura(m) : '))
peso = int(input('Informe o seu peso(kg) : '))
classificacao = None
teste = None

while teste != 'valid':
    imc = peso / (altura * altura)
    if 16 < imc < 16.9:
        classificacao = 'Muito abaixo do peso'
        teste = 'valid'
    elif 17 < imc < 18.4:
        classificacao = 'Abaixo do peso'
        teste = 'valid'
    elif 18.5 < imc < 24.9:
        classificacao = 'Peso normal'
        teste = 'valid'
    elif 25 < imc < 29.9:
        classificacao = 'Acima do peso'
        teste = 'valid'
    elif 30 < imc < 34.9:
        classificacao = 'Obesidade grau I'
        teste = 'valid'
    elif 35 < imc < 40:
        classificacao = 'Obesidade grau II'
        teste = 'valid'
    elif 40 < imc:
        classificacao = 'Obesidade grau III'
        teste = 'valid'    
    else:
        print('\n\nTivemos um problema para calcular o seu IMC')
        altura = float(input('Informe novamente sua altura(m) : '))
        peso = int(input('Informe novamente o seu peso(kg) : '))

print('\n\nO valor do seu IMC e: {}\nVoce foi classificado como: {}'.format(imc,classificacao))


