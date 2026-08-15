def remover_par():
    numeros = list(range(1, 11))
    numeros.append(11) # Adiciona o número 11 à lista
    
    print("Lista original:", numeros)
    
    # Cria uma nova lista mantendo apenas os ímpares
    numeros_impares = [n for n in numeros if n % 2 != 0]
    
    return numeros_impares  # Retorna a lista filtrada

numeros = remover_par()
print("Lista após remover números pares:", numeros)


# testando alterar tuplas

coordenadas = (10, 20)

try:
    coordenadas[0] = 0
except TypeError:
    print("Não é possível alterar uma tupla, pois ela é imutável.")    


# Convertendo tupla em lista 

notas = (7.5, 8.0, 9.0)

notas_lista = list(notas)  # Converte a tupla em lista
notas_lista.append(10.0)  # Adiciona um novo elemento à lista

media = sum(notas_lista) / len(notas_lista)  # Calcula a média das notas
print(f"Nova lista de notas: {notas_lista}")
print(f"Média das notas: {media}")


numeros_inteiros = (1, 2, 3, 4, 5)

soma = sum(numeros_inteiros)  # Calcula a soma dos elementos da tupla

print(f"Soma dos números inteiros: {soma}")


# Coordenadas usando tuplas

def coordenadas():
    return (10, -4.5, 30)

x, y, z = coordenadas()

print(f"Coordenada de X: {x}")
print(f"Coordenada de Y: {y}")
print(f"Coordenada de Z: {z}")


# Retirando elementos replicados de uma lista

numeros_replicados = [1, 2, 3, 2, 4, 1, 5]
unicos = []

for numero in numeros_replicados:
   if numero not in unicos:
       unicos.append(numero)

print(f"Números únicos: {unicos}")

# Retirando elementos replicados de uma lista e colocando frequencia

linguagens = ["Python", "Java", "C++", "Python", "JavaScript", "C++", "Java"]
nova_lista_linguagens = []
frequencia = []

for n in linguagens:
 if n not in nova_lista_linguagens:
       nova_lista_linguagens.append(n)
       frequencia.append(linguagens.count(n)) # adiciona a frequencia de cada elemento na lista frequencia

print("Linguagens únicas:", nova_lista_linguagens, "Frequência:", frequencia)       