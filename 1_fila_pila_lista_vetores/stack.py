# LISTA 1, QUESTÃO CADERNO INTELIGENTE
class Stack:  # classe da pilha
    def __init__(self):
        self.top = None
        self.size = 0
        self.data = []

    def __len__(self):
        return self.size

    def push(self, i):
        self.data.append(i)
        self.size = self.size + 1

    def pop(self):
        self.size = self.size - 1
        return self.data.pop()

    def peek(self):
        if not self.data:
            return []
        else:
            return self.data[-1]

# funções de checagem
def errorFinder(lista):  # vcount != fcount
    lista1 = list(lista)
    pairs = True
    num_f = 0
    num_v = 0
    while pairs == True:

        for item in lista:

            if item == 'F':
                lista.remove(item)
                pairs = False
                num_f += 1

                for i in lista:
                    if i == 'V':
                        lista.remove(i)
                        pairs = True
                        num_v += 1

                        break

                break
    position = 0

    for j in lista1:
        if num_f > 0:
            if j == 'F':
                position += 1
                num_f -= 1
            else:
                position += 1

    return position


def errorCheck(lista):  # vcount == fcount
    lista = lista
    og_size = int(len(lista))
    correct = True
    while len(lista) > 0 and correct == True:

        for item in lista:

            if item == 'F':
                lista.remove(item)

                for i in lista:
                    if i == 'V':
                        lista.remove(i)
                        break

                break

            elif item == 'V':
                correct = False
                position = og_size - len(lista) + 1
                break

    if correct == True:
        return 'undefined'
    else:
        return position


# input
paginas = list(input())
correct = True
pilha = Stack()
vcount = 0
fcount = 0

for item in paginas:  # criar stack
    pilha.push(item)
    if item == 'V':
        vcount += 1
    if item == 'F':
        fcount += 1

# checar stack
if pilha.size == 1:
    correct = False
    x = 1

else:
    if vcount != fcount:  # finding error: quantidade de Vs != Fs
        correct = False

        if vcount < fcount:
            x = (errorFinder(paginas))

        elif vcount > fcount:
            x = (errorCheck(paginas))


    else:  # finding error: quantidade de Vs == Fs
        last_peek = pilha.peek()
        if last_peek == 'F':
            correct = False
            x = pilha.size

        else:
            if paginas[0] == 'V':
                correct = False
                x = 1

            else:
                x = errorCheck(paginas)
                if x != 'undefined':
                    correct = False

# output
if correct:
    print('Correto.')
else:
    print(f'Incorreto, devido a capa na posição {x}.')
    
print(pilha.data)
