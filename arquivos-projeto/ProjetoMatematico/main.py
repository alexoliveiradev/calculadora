def multiplos():
    numero = int(input('Informe o número: '))
    mult = int(input('Quantos múltiplos deseja ver? '))
    total = list()
    cont = 1
    while True:
        if len(total) == mult:
            break
        else:
            num = numero * cont
            total.append(num)
            cont += 1
    print(f'Esses são os múltiplos de {numero}:\n{total}')


def bhaskara():
    while True:
        print('Calculando as raízes de uma equação de 2º grau\n')

        a = float(input('Digite o valor de A: '))
        b = float(input('Digite o valor de B: '))
        c = float(input('Digite o valor de C: '))

        delta = (b ** 2) - (4 * a * c)

        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)

        print(f'\nValor de x1: {x1}')
        print(f'Valor de x2: {x2}')

        continua = input('\nDeseja continuar? Digite q ou Enter para um novo cálculo: \n')
        if continua == 'q':
            break


def fibonacci():
    while True:
        x = int(input('\nQuantos termos você quer ver? (0) para sair\nSua resposta: '))
        if x == 0:
            break
        else:
            a = 0
            b = 1

            print(f'{a} {b} ', end='')

            for i in range(2, x):
                c = a + b
                print(f'{c}', end=' ')
                a = b
                b = c


def entrada(num):
    if num == 1:
        vezes = int(input('Total de números a serem somados: '))
        valores = list()
        for i in range(vezes):
            x = float(input(f'{i + 1}° número: '))
            valores.append(x)

        print(f'SOMA DOS NÚMEROS: {valores}')
        print(f'RESULTADO: {sum(valores)}\n')

    elif num == 2:
        vezes = int(input('Total de números a serem subtraidos: '))
        valores = list()
        for i in range(vezes):
            x = float(input(f'{i + 1}° número: '))
            valores.append(x)

        total = float()
        for i in range(len(valores)):
            if i == 0:  # Condição para o total não ser negativo sempre
                total = valores[i]
            else:
                total -= valores[i]

        print(f'SUBTRAÇÃO DOS NÚMEROS: {valores}')
        print(f'RESULTADO: {total}\n')

    elif num == 3:
        vezes = int(input('Total de números a serem multiplicados: '))
        valores = list()

        for i in range(vezes):
            x = float(input(f'{i + 1}º número: '))
            valores.append(x)

        total = 0
        for num in range(len(valores)):
            if num == 0:  # Sem esta condição o resultado sempre será 0
                total = valores[num]
            else:
                total *= valores[num]

        print(f'MULTIPLICAÇÃO DOS NÚMEROS: {valores}')
        print(f'RESULTADO: {total}\n')

    elif num == 4:
        vezes = int(input('Total de números a serem dividos: '))
        valores = list()

        for i in range(vezes):
            x = float(input(f'{i + 1}º número: '))
            valores.append(x)

        total = 0
        for num in range(len(valores)):
            if num == 0:  # Esta condição impede que haja a divisão por zero no início
                total = valores[num]
            else:
                total /= valores[num]

        print(f'DIVISÃO DOS NÚMEROS: {valores}')
        print(f'RESULTADO: {total}\n')

    elif num == 5:
        vezes = int(input('Total de números para a exponenciação: '))
        valores = list()

        total = list()
        for i in (range(vezes)):
            print(f'==={i + 1}º número===')
            x = float(input('1° número (base): '))
            y = float(input('2° número (expoente): '))
            total_valores = x ** y
            total.append(total_valores)
            valores.append(x)

        print(f'EXPONENCIAÇÃO DOS NÚMEROS: {valores}')
        print(f'RESULTADO: {total}\n')

    elif num == 6:
        vezes = int(input('Total de números a serem calculos a raiz quadrada: '))
        valores = list()

        total = list()
        for i in range(vezes):
            x = float(input(f'{i + 1}º número: '))
            raiz = x ** (1 / 2)
            valores.append(x)
            total.append(raiz)

        print(f'RAIZ QUADRADA DOS NÚMEROS: {valores}')
        print(f'RESULTADO: {total}\n')

    elif num == 7:
        # Fazer a fatoração
        vezes = int(input('Total de números a serem calculos a raiz cúbica: '))
        valores = list()

        total = list()
        for i in range(vezes):
            x = float(input(f'{i + 1}º número: '))
            raiz = x ** (1 / 3)
            valores.append(x)
            total.append(raiz)

        print(f'RAIZ CÙBICA DOS NÚMEROS: {valores}')
        print(f'RESULTADO: {total}\n')


def menusecund():
    while True:
        print('\nQual das operações matemáticas você deseja fazer?\n'
              '1 - Soma\n'
              '2 - Subtração\n'
              '3 - Multiplicação\n'
              '4 - Divisão\n'
              '5 - Exponenciação\n'
              '6 - Raiz Quadrada\n'
              '7 - Raiz Cúbica\n'
              '0 - Voltar para ao menu anterior\n')
        escolha = int(input('Informe sua escolha: '))
        if escolha == 0:
            break
        elif escolha == 1:
            entrada(escolha)
        elif escolha == 2:
            entrada(escolha)
        elif escolha == 3:
            entrada(escolha)
        elif escolha == 4:
            entrada(escolha)
        elif escolha == 5:
            entrada(escolha)
        elif escolha == 6:
            entrada(escolha)
        elif escolha == 7:
            entrada(escolha)


def menuprinc():
    while True:
        print('======MENU PRINCIPAL======')
        print('1 - Cálculos simples\n'
              '2 - Fórmula de Bhaskara\n'
              '3 - Múltiplo\n'
              '4 - Sequência Fibonacci\n'
              '0 - Fechar Menu')

        escolha = int(input('\nInforme sua escolha: '))

        if escolha == 0:
            break
        elif escolha == 1:
            menusecund()
        elif escolha == 2:
            bhaskara()
        elif escolha == 3:
            multiplos()
        elif escolha == 4:
            fibonacci()
        else:
            print('Escolha inválida!')


while True:
    try:
        print(f"{'=' * 5}CÁLCULOS MATEMÁTICOS{'=' * 5}")
        opcao = int(input('1 - Prosseguir\n0 - Finalizar o programa\nSua escolha: '))
        if opcao == 1:
            menuprinc()
        else:
            break
    except ValueError:
        print('Por favor digite um número válido.')
    except TypeError:
        pass
