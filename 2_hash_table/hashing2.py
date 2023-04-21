# LISTA 3, QUESTÂO NAVEGAÇÃO ESPACIAL 
# Classes e métodos
class HashMap:
    def __init__(self):
        self.size = 0
        self.data = None
        self.memoria = True

    def hashFunction(self, key, index):  # função
        length = self.size
        return (key + index) % length

    def insert(self, chave):  # inserir, retorna o index na qual foi inserido a chave
        self.memoria = self.mDisponivel()
        if self.memoria:
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

            return slot

    def hashSearch(self, chave):  # procurar, retorna None caso a chave não exista ou o index onde a chave se encontra
        idx = 0
        position = None
        og_slot = self.hashFunction(chave, idx)
        if self.data[og_slot] == chave:  # chave está em seu lugar originário
            return og_slot

        else:
            while position != og_slot:
                idx += 1
                new_slot = self.hashFunction(chave, idx)
                position = new_slot
                if self.data[new_slot] == chave:
                    return new_slot

            return None

    def indexSearch(self, idx):  # procurar, retorna o conteúdo do index (slot) ou None caso não haja
        slot = self.data[idx]
        return slot

    def mDisponivel(self):  # verifica a memória disponível
        check = False
        for item in self.data:
            if item is None:
                check = True

        return check


# Operações
datacenter = HashMap()
datacenter.size = int(input())
datacenter.data = [None] * datacenter.size

num_comandos = int(input())
while num_comandos != 0 and datacenter.memoria:
    datacenter.memoria = datacenter.mDisponivel()
    entrada = input().split(' ')
    comando, chave = entrada[0], int(entrada[1])
    if comando == 'ADD':  # inserir
        adicionar = datacenter.insert(chave)
        print(f'E: {adicionar}')

    elif comando == 'SCH':  # search by key
        procurar = datacenter.hashSearch(chave)
        if procurar == None:
            print('NE')

        else:
            print(f'E: {procurar}')

    elif comando == 'CAP':  # search by index
        procurar = datacenter.indexSearch(chave)
        if procurar is None:
            print(f'D')

        else:
            print(f'A: {procurar}')

    num_comandos -= 1

if not datacenter.memoria:
    print(f'Toda memoria utilizada')
