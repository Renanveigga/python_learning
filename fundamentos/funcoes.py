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

notas = [float(input("Digite a nota do aluno: ")) for _ in range(3)]

def calculo_de_notas(notas):
    media = sum(notas) / len(notas)
    if media >= 60:
        status = "Aprovado"
    else:
        status = "Reprovado"
    return media, status

media_aluno, resultado = calculo_de_notas(notas)

print(f"A média das notas é {media_aluno:.2f} e o aluno está {resultado}.")     
 

def adivinhe_o_numrero():
    import random
    numero_secreto = random.randint(1, 10)
    tentativas = 0

    while tentativas < 3:
     numero = int(input("tente acertar o número entre 1 e 10: "))
     if numero == numero_secreto:
        print("Parabéns! Você acertou o número secreto!")
        return # encerrar a função após o acerto
     elif numero < numero_secreto:
        print("O número secreto é maior. Tente novamente.")
        tentativas += 1
     else:
        print("O número secreto é menor. Tente novamente.")
        tentativas += 1
    print(f"As tentativas acabaram. O número secreto era {numero_secreto}.")    

adivinhe_o_numrero()



def criar_senha_forte():
    import random # importa a biblioteca random para gerar números aleatórios
    import string # importa a biblioteca string para gerar caracteres aleatórios

    senha = input("Digite uma senha: ")
    print("senha fraca")

    sugestao = input("Deseja uma sugestão de senha forte? (s/n): ")
    if sugestao.lower() == 's':
        caracteres = string.ascii_letters + string.digits + string.punctuation + string.digits # gera carateres aleatórios para a senha
        senha_forte = ''.join(random.choice(caracteres) for _ in range(12))  #escolhe 12 caracteres aleatórios da lista de caracteres
        print(f"Sugestão de senha forte: {senha_forte}")
        return senha_forte

criar_senha_forte()        


estoque = []

def adicionar_produto():
    produto = input("Digite um produto para adicionar ao estoque: ")
    confirmacao = input(f"Deseja adicionar {produto} ao estoque? (s/n): ")

    if confirmacao.lower() == "s":
        estoque.append(produto) # append adiciona item no final da lista
        print(f"{produto} adicionado ao estoque.")
    else:
        print(f"{produto} não foi adicionado ao estoque.")
        return

    mostrar_estoque = input("Deseja ver o estoque atual? (s/n): ")
    if mostrar_estoque.lower() == "s":
        print("Estoque atual:", estoque)


adicionar_produto()            



