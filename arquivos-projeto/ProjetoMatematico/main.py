def multiplos():
    while True:
        numero = int(input("Digite um número: "))
        mult = [numero * i for i in range(11)]  # Começo o range em 0 porque zero é múltiplo de todo número inteiro
        print(f"Esses são os múltiplos de {numero}:\n{mult}\n")
        continuar = input("(Enter) para um novo cálculo ou (0) para sair: ")
        if continuar == '0':
            break

def bhaskara():
    print('Digite os valores de A, B e C')
    while True:

        a = float(input('A: '))
        b = float(input('B: '))
        c = float(input('C: '))

        delta = (b ** 2) - (4 * a * c)

        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)

        #return f'\nValor de x1: {x1}\nValor de x2: {x2}'
        print(f'\nValor de x1: {x1}\nValor de x2: {x2}')

        continua = input("\n(Enter) para um novo cálculo ou (0) para sair: ")
        if continua == '0':
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
        numeros = list()
        print("A QUALQUER MOMENTO DIGITE (0) PARA PARAR!")
        while True:
            print(f"Total da soma -> {sum(numeros)}")
            valor = float(input('Número: '))
            if valor != 0:
                numeros.append(valor)
            else:
                break

    elif num == 2:
        numeros = list()
        print("A QUALQUER MOMENTO DIGITE (0) PARA PARAR!")
        while True:
            x = float(input("Número: "))
            if x != 0:
                numeros.append(x)
            else:
                break
    
        total = 0  # Caso a variável não fosse declarada anteriormente geraria um erro.
        for i in range(len(numeros)):
            if i == 0:  # Condição para o total não ser negativo sempre
                total = numeros[i]
            else:
                total -= numeros[i]

        print(f'SUBTRAÇÃO DOS NÚMEROS: {numeros}')
        print(f'RESULTADO: {total}\n')

    elif num == 3:
        vezes = int(input('Total de números a serem multiplicados: '))
        valores = list()

        for i in range(vezes):
            x = float(input(f'{i + 1}º número: '))
            valores.append(x)

        total = 0
        for num in range(len(valores)):
            if num == 0:  # Sem essa condição o resultado sempre será 0
                total = valores[num]
            else:
                total *= valores[num]

        print(f'MULTIPLICAÇÃO DOS NÚMEROS: {valores}')
        print(f'RESULTADO: {total}\n')

    elif num == 4:
        vezes = int(input('Total de números a serem divididos: '))
        valores = list()

        for i in range(vezes):
            x = float(input(f'{i + 1}º número: '))
            valores.append(x)

        total = 0
        for num in range(len(valores)):
            if num == 0:  # Essa condição impede que haja a divisão por zero no início
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
        vezes = int(input('Total de números a serem calculados a raiz quadrada: '))
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
        vezes = int(input('Total de números a serem cálculos a raiz cúbica: '))
        valores = list()

        total = list()
        for i in range(vezes):
            x = float(input(f'{i + 1}º número: '))
            raiz = x ** (1 / 3)
            valores.append(x)
            total.append(raiz)

        print(f'RAIZ CÚBICA DOS NÚMEROS: {valores}')
        print(f'RESULTADO: {total}\n')


def menusecundario():
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
        else:
            entrada(escolha)


def menuprincipal():
    while True:
        print('MENU PRINCIPAL')
        print('1 - Cálculos simples\n'
              '2 - Fórmula de Bhaskara\n'
              '3 - Múltiplos\n'
              '4 - Sequência Fibonacci\n'
              '0 - Sair')

        escolha = int(input('\nInforme sua escolha: '))

        if escolha == 0:
            break
        elif escolha == 1:
            menusecundario()
        elif escolha == 2:
            bhaskara()
        elif escolha == 3:
            multiplos()
        elif escolha == 4:
            fibonacci()
        else:
            print('Escolha inválida!')

def bem_vindo():
    print(f"{'='*5}BEM VINDO A CALCULADORA!{'='*5}\n")
    menuprincipal()


bem_vindo()
