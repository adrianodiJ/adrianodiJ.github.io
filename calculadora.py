import math

# Funções matemáticas
def soma(num1, num2):
    return num1 + num2

def subtracao(num1, num2):
    return num1 - num2

def multiplicacao(num1, num2):
    return num1 * num2

def divisao(num1, num2):
    if num2 == 0:
        return "Erro: Divisão por zero!"
    return num1 / num2

def potencia(num1, num2):
    return num1 ** num2

def divisao_com_resto(num1, num2):
    return num1 % num2

def divisao_inteira(num1, num2):
    return num1 // num2

def porcentagem(num1, num2):
    return (num1 * num2) / 100
#------------------------------------------------
def calcular_desconto(valor, desconto):
    return valor - ((valor * desconto) / 100)

def raiz_quadrada(numero):
    if numero < 0:
        return "Erro: Número negativo!"
    return math.sqrt(numero)

def bhaskara(a, b, c):
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Não há raízes reais"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Raiz única: x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Raízes reais: x1 = {x1}, x2 = {x2}"

def razao (a,b):
    r = (a/b) *100
    return r

def regra_de_tres(a,b,c):
    r = (a*c)/b
    return r

def proporção(a,b,c):
    print("Selecione o tipo da regra de três:")
    print("A - Diretamente proporcional.")
    print("B - Inversamente proporcional.")

    opcao_a = "A"
    opcao_b = "B" 
    regra_tres = input("insira A ou B: ")

    if regra_tres == opcao_a.lower():
        r = a*c / b
        return r
    if regra_tres == opcao_b.lower():
        r = a*b /c
        return r
    
def conjuntos(a, b):
    resultado = input("Escolha qual você quer: [1]uniao, [2]intersecao, [3]diferenca: ").strip().lower()
    
    if resultado == '1':
        return a | b 
    elif resultado == '2':
        return a & b 
    elif resultado == '3':
        return a ^ b 
    else:
        return "Opção inválida"




# Início do programa
historico = []

while True:
    print("\n=== CALCULADORA COMPLETA ===")
    print("[1] Operações Simples")
    print("[2] Operações Complexas")
    print("[3] Histórico")
    print("[4] Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':  # Operações Simples
        print("\n--- Operações Simples ---")
        print("[1] Soma")
        print("[2] Subtração")
        print("[3] Multiplicação")
        print("[4] Divisão")
        print("[5] Potência")
        print("[6] Divisão com Resto")
        print("[7] Divisão Inteira")
        print("[8] Porcentagem")

        opcao = input("Escolha a operação: ")
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        operacoes = {
            '1': ("Soma", soma(num1, num2)),
            '2': ("Subtração", subtracao(num1, num2)),
            '3': ("Multiplicação", multiplicacao(num1, num2)),
            '4': ("Divisão", divisao(num1, num2)),
            '5': ("Potência", potencia(num1, num2)),
            '6': ("Divisão com Resto", divisao_com_resto(num1, num2)),
            '7': ("Divisão Inteira", divisao_inteira(num1, num2)),
            '8': ("Porcentagem", porcentagem(num1, num2))
        }

        if opcao in operacoes:
            operacao, resultado = operacoes[opcao]
            print(f"Resultado da {operacao}: {resultado}")
            historico.append(f"{operacao}: {num1} e {num2} = {resultado}")
        else:
            print("Opção inválida!")

    elif escolha == '2':  # Operações Complexas
        print("\n--- Operações Complexas ---")
        print("[1] Bhaskara")
        print("[2] Raiz Quadrada")
        print("[3] Calcular Desconto")
        print("[4] Razão")
        print("[5] Regra de Três")
        print("[6] Proporção")
        print("[7] Conjuntos")
        print("[8] Expressão Algebrica")
        print("[9] Sistema Linear")

        opcao = input("Escolha a operação: ")

        if opcao == '1':
            print("\n=== Bhaskara ===")
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))
            resultado = bhaskara(a, b, c)
            print(f"Resultado: {resultado}")
            historico.append(f"Bhaskara para ({a}, {b}, {c}) = {resultado}")

        elif opcao == '2':
            print("\n=== Raiz Quadrada ===")
            num = float(input("Digite o número: "))
            resultado = raiz_quadrada(num)
            print(f"Resultado: {resultado}")
            historico.append(f"Raiz Quadrada de {num} = {resultado}")

        elif opcao == '3':
            print("\n=== Calcular Desconto ===")
            valor = float(input("Digite o valor original: "))
            desconto = float(input("Digite a porcentagem de desconto: "))
            resultado = calcular_desconto(valor, desconto)
            print(f"Valor final com desconto: {resultado}")
            historico.append(f"Desconto de {desconto}% sobre {valor} = {resultado}")

        elif opcao =='4':
            print("\n=== Razão ===")
            valor_a = float(input("Digite o primeiro valor: "))
            valor_b = float(input("Digite o segundo valor: "))
            resultado = razao(a,b)
            print(f"A razão é: {resultado}")
            historico.append(f"O valor {valor_a} sobre {valor_b} = {resultado}")

        elif opcao =='5':
            print("\n=== Regra de Três ===")
            valor_a = float(input("Digite o 1ºvalor: "))
            valor_b = float(input("Digite o 2ºvalor: "))
            valor_c = float(input("Digite o 3ºvalor: "))
            resultado = regra_de_tres(a,b,c)
            print(f"O resultado da Regra de Três é: {resultado}")
            historico.append(f"O resolução dos valores {valor_a} , {valor_b} , {valor_c} = {resultado} ")
        
        elif opcao =='6':
            print("\n=== Proporção ===")
            a = float(input("Digite o 1ºvalor: "))
            b = float(input("Digite o 2ºvalor: "))
            c = float(input("Digite o 3ºvalor: "))
            resultado = proporção(a,b,c)
            print(f"O resultado da Proporção é: {resultado}")
            historico.append(f"O Resultado de {a}, {b} e {c} = {resultado}")
        
        elif opcao =='7':
            print('Conjuntos')
            a = set(map(int,input("Digite os elementos do 1º conjunto separados por vírgula: ").split(',')))
            b = set(map(int,input("Digite os elementos do 2º conjunto separados por vírgula: ").split(',')))
            resultado = conjuntos(a, b)
            print(f"Resultado: {resultado}")
            historico.append(f"O resultado de {a} e {b} = {resultado}")
            

        elif opcao =='8':
            print("\n=== Expressão Algebrica ===")
            from sympy import symbols, simplify, expand, sympify
            import re
            x, y = symbols('x y')
            def formatar_expressao(expr):
                """Adiciona '*' automaticamente entre números e variáveis"""
                return re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
            print('Expressão algebrica!')
            expr1 = sympify(formatar_expressao(input('Escreva a primeira expressão: ')))
            expr2 = sympify(formatar_expressao(input('Escreva a segunda expressão: ')))

            x = symbols('x')
            y = symbols('y')

            condicao = input('Escolha o tipo de operação:\n'
                            '[1] - Soma\n'
                            '[2] - Subtração\n'
                            '[3] - Multiplicação\n'
                            '[4] - Divisão\n'           
            '')
            if condicao == '1':
                resultado = expr1 + expr2
                print(f'Resultado: {resultado}')
                
            if condicao =='2':
                resultado = simplify(expr1 - expr2)
                print(f'O Resultado é:{resultado}')
                
            if condicao =='3':
                resultado = expand(expr1 * expr2)
                print(f'O resultado é: {resultado}')

            if condicao =='4':
                resultado = simplify(expr1/expr2)
                print(f'O resultado é: {resultado}')
        
        elif opcao =='9':
            import numpy as np
            A = np.zeros((2, 2))
            B = np.zeros(2)

            print("Digite os coeficientes dos dois sistemas (os 2 numeros da linha de cima e os 2 da linha de baixo) UM POR UM!: ")
            for i in range(2):
                for j in range(2):
                    A[i, j] = float(input(f"Digite A:"))

            print("Digite os resultados dos dois sistemas: ")
            for i in range(2):
                B[i] = float(input(f"Digite B[{i+1}]: "))

            try:
                X = np.linalg.solve(A, B)
                print("\nSolução do sistema:")
                for i in range(2):
                    print(f"x{i+1} = {X[i]}")
            except np.linalg.LinAlgError:
                print("O sistema não tem solução única ou é inválido.")

        else:
            print("Opção inválida!")

    elif escolha == '3':  # Histórico
        if not historico:
            print("\nHistórico está vazio!")
        else:
            print("\n=== Histórico de Cálculos ===")
            for i, item in enumerate(historico, 1):
                print(f"{i}. {item}")

    elif escolha == '4':  # Sair
        print("\nVOCE ESTÁ SAINDO, OBG PELA PREFERÊNCIA!!!!")
        print("\n ----- Criadores -----")
        print("--- ADRIANO DIAS ---") 
        print("--- JOÃO ACERBI ---")
        print("--- GABRIEL LACERDA ---")
        print("--- RAFAEL BOTTI ---")
        print("--- DANILO AZEVEDO ---")
        break

    else:
        print("Opção inválida! Tente novamente.")