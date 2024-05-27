from thread import ThreadWithReturnValue


def calculaArray(lista):
    res = 0
    for i in range(len(lista)):
        res += lista[i]
    return res


p1 = ThreadWithReturnValue(target=calculaArray,  args=([1, 2, 10, 20, 61],))

p2 = ThreadWithReturnValue(target=calculaArray, args=([3, 6, 9, 17, 64],))

p1.start()
p2.start()
result = p1.join()
result2 = p2.join()
resultFinal = result + result2

print("soma da thread 1 '",result,"', com a thread 2 '",result2,"' =", resultFinal)


