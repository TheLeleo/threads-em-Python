from thread import ThreadWithReturnValue


def retornaNome(name):
    return name


p1 = ThreadWithReturnValue(target=retornaNome,  args=("melis",))

p2 = ThreadWithReturnValue(target=retornaNome, args=("lelis",))

p1.start()
p2.start()
result = p1.join()
result2 = p2.join()

print(result, " ", result2)

