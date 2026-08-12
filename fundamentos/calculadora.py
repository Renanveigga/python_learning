def soma (a,b):
    return a + b

def subtracao(a,b):
    return a - b

def multiplicacao(a,b):
    return a * b

def divisao(a,b):
    return a / b

def potencia(a,b):
    return a ** b

print("Calculadora")
print("Escolha a operação:")
print("1. Soma")    
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Potência")

escolha = int(input("Digite a opção (1/2/3/4/5): "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if escolha == 1:
    print(f"{num1} + {num2} = {soma(num1, num2)}")

if escolha == 2:    
    print(f"{num1} - {num2} = {subtracao(num1, num2)}")

if escolha == 3:
    print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")

if escolha == 4:
    print(f"{num1} / {num2} = {divisao(num1, num2)}")

if escolha == 5:
    print(f"{num1} ** {num2} = {potencia(num1, num2)}")