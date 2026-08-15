# laço de repetição do 1 até o 10

for i in range(1, 11):
    print(i)

# Exemplo de laço de repetição com número par

for i in range(50):
    if i % 2 == 0:
        print(i, "é par")

# Exemplo de laço de repetição com número ímpar

for i in range(50):
    if i % 2 != 0:
        print(i, "é ímpar")

#contagem regressiva

for i in range(10, 0, -1):
    print(i)

# Tabuada

numero  = int(input("Digite um número: "))

for i in range(11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")