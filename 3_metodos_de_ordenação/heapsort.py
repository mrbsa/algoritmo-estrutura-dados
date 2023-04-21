# LISTA 4, QUESTÃO WOLFMAN AGENDA
# Funções das propriedades do HeapSort
def getParent(i):  # retorna index do pai do nó de index i
    function = i / 2
    if function % 2 == 0:
        return function

    else:  # função piso
        return (i - 1) / 2

def getLeftson(i):  # retorna o index do filho esquerdo do nó de index i
    return 2 * i + 1

def getRightson(i):  # retorna o index do filho direito do nó de index i
    return 2 * i + 2

# criação da árvore Heap
def maxHeapify(lista, i):  # ordena o vetor no estilo Heapmax
    size = len(lista)
    l = getLeftson(i)
    r = getRightson(i)
    if l < size and lista[l] > lista[i]:
        maior = l

    else:
        maior = i

    if r < size and lista[r] > lista[maior]:
        maior = r

    if maior != i:  # fora da ordem
        lista[i], lista[maior] = lista[maior], lista[i]
        maxHeapify(lista, maior)  # recursiva até a ordenação

def maxBuilder(lista):  # constrói a Heapmax
    size = len(lista)
    halfsize = int((size / 2) - 1)

    for item in range(halfsize, -1, -1):  # percorre da metade até o início de trás pra frente
        maxHeapify(lista, item)

def maxExtract(lista):  # remove e retorna o item de maior valor (a raíz)
    if len(lista) > 0:
        maxx = lista.pop(0)
        maxBuilder(lista)

        return maxx

def getMin(lista):   # retorna o valor mínimo do vetor
    if len(lista) > 0:
        def iteration(lista):  # itera somente as folhas do vetor
            lastP = (len(lista) - 2) // 2
            firstL = lastP + 1
            leaves = [lista[i] for i in range(firstL, len(lista))]

            return leaves

        def minHelper(lista):  # auxilia na identificação do valor mínimo
            leaves = iteration(lista)
            minn = leaves[0]
            for leaf in leaves:
                if leaf < minn:
                    minn = leaf

            return minn

        return minHelper(lista)



# Entradas
sequencia = input().split(' ')  # input
constante = int(input())
for string in sequencia:  # remove strings vazias residuais
    if string == '':
        sequencia.remove(string)

numeros = [int(num) for num in sequencia]  # converte lista de strings em lista de inteiros
maxBuilder(numeros)  # chama a função Heap


# Operações
rodada = 0
while len(numeros) > 0:
    maximum = maxExtract(numeros)
    if len(numeros) >= 1:
        minimum = getMin(numeros)
        K = int(maximum - abs(minimum * constante))  # módulo
        if K > 0:
            numeros.append(K)
            maxBuilder(numeros)

    rodada += 1

print(f'{rodada} rodadas, partindo para a próxima!')  # output
