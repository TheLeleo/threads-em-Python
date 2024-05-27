from thread import ArquiteturaThread # importar classe ArquiteturaThread dentro do arquivo thread.py


# Funções globais
ARRAY1 = [1, 2, 10, 20, 61]
ARRAY2 = [3, 6, 9, 17, 64]


# Função que recebe um array e calcula a soma de todos os valores
def calculaArray(lista):
    res = 0
    for i in range(len(lista)):
        res += lista[i]
    return res

# criando 2 threads com a função de calculaArray, inserindo os respectivos arrays
processo1 = ArquiteturaThread(target=calculaArray,  args=(ARRAY1,))
processo2 = ArquiteturaThread(target=calculaArray, args=(ARRAY2,))
processo3 = ArquiteturaThread(target=calculaArray, args=(ARRAY2,))

# iniciando as threads
processo1.start()
processo2.start()
processo3.start()

# armazenando os resultados
resultado1 = processo1.getResult()
resultado2 = processo2.getResult()
resultado3 = processo2.getResult()

# Realizar as somas dos resultados obtidos pelas 2 threads
resultFinal = resultado1 + resultado2
resultFinal += resultado3

# Printar os resultados no terminal
#print("soma da thread 1 (", resultado1, "), com a thread 2 (", resultado2, ") =", resultFinal)
print("soma da thread 1 (", resultado1, "), com a thread 2 (", resultado2,") juntamente com a thread 3 (", resultado3, ") =", resultFinal)