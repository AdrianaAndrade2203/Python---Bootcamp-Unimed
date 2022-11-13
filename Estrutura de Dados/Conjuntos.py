#Conjuntos - Criando sets - Sets é uma colecao que nao possui elementos repetidos.

numeros = set([1, 2, 2, 3, 4, 5])
print(numeros)

for numero in numeros:
    print(numero)

frutas = set("abacaxi")
print(frutas)

veiculos = set(("palio", "gol", "celta", "palio"))
print(veiculos)

for indice, carro in enumerate(veiculos):
    print(f"{indice}: {carro}")

#Conjuntos em python nao suportam indexação e nem fatiamento. Para isso será necessária conversão em lista

numeros = list(numeros)
print(numeros[0])

#Metodos da classe set: 

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a_b = conjunto_a.union(conjunto_b)
print(conjunto_a_b)

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a_b = conjunto_a.intersection(conjunto_b)
print(conjunto_a_b)

#Neste caso irá retornar o que nao esta no conjunto B. O que tem no A que nao tem no B. 

conjunto_a_b2 = conjunto_a.difference(conjunto_b)
print(conjunto_a_b2)

#Se quiser todos os elemntos usar o metodos symmetric_difference

diferenca_conjuntos = conjunto_a.symmetric_difference(conjunto_b)
print(diferenca_conjuntos)

#Add - Para adicionar elementos

sorteio = {1, 20}

sorteio.add(25)
print(sorteio)
print(len(sorteio))

#Para saber se um numero esta no conjunto

print (1 in sorteio)
print (25 in sorteio)
print (30 in sorteio)




