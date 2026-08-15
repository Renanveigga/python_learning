n = int(input("Digite um número para calcular o fatorial: "))


def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

resultado = fatorial(n)
print(f"O fatorial de {n} é {resultado}")    


def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True