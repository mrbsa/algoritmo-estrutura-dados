# LISTA 3, QUESTÂO CAFÉPASS
# Classes e métodos
class HashMap:
    def __init__(self):
        self.size = 0
        self.data = None

    def hashFunction(self, key, index):  # função
        length = self.size
        return (key + index) % length

    def insert(self, chave):  # inserir
        index = 0
        slot = self.hashFunction(chave, index)
        if self.data[slot] is None:  # insere no espaço vazio
            self.data[slot] = chave

        else:  # espaço não está vazio, pula para o próximo
            while self.data:
                index += 1
                slot = self.hashFunction(chave, index)
                if self.data[slot] is None:
                    self.data[slot] = chave
                    break

    def hashSearch(self, chave):  # procurar
        idx = 0
        position = None
        og_slot = self.hashFunction(chave, idx)
        if self.data[og_slot] == chave:  # chave está em seu lugar originário
            return True

        else:
            while position != og_slot:
                idx += 1
                new_slot = self.hashFunction(chave, idx)
                position = new_slot
                if self.data[new_slot] == chave:
                    return True

            return False


# Funções independentes
def arrayCreator(numeros):  # retorna uma lista com valores baseados no CPF
    num0, num1, num2 = list(numeros), [], []
    for item in num0:  # multiplica cada dígito por 10
        i = int(item)
        num1.append(i * 10)

    while len(num1) > 0:  # acha valores duplicados e soma-os
        count = 1
        i = num1.pop(0)
        new_sum = False
        try:
            while True:
                num1.remove(i)
                new_sum = True
                count += 1

        except ValueError:
            pass

        if new_sum:
            num2.append(i * count)

        else:
            num2.append(i)

    return num2


def addition(numeros):  # retorna as diferentes possibilidades de soma em lista
    lista_soma = []
    count = 1
    for i in numeros:

        for j in numeros[count::]:
            if i != j:
                new_sum = int(i + j)

                if new_sum not in lista_soma:
                    lista_soma.append(new_sum)

        count += 1

    return lista_soma


# Operações
N = int(input())
while N != 0:
    cpf_mn = input().split(' ')  # formatação do input
    CPF, magicN = cpf_mn[0], int(cpf_mn[1])

    somas = arrayCreator(CPF)
    chaves = addition(somas)

    table = HashMap()  # criação da hash table
    table.size = len(chaves)
    table.data = [None] * table.size
    for item in chaves:
        table.insert(item)

    if table.hashSearch(magicN):  # output
        print('UP Permission')

    else:
        print('NOT Permission')

    N -= 1
    