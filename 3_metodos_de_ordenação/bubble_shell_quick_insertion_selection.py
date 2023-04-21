# LISTA 4, QUESTÃO PACIÊNCIA INFINITA
# Funções de ordenação
def bubbleSort(lista, interrompimento, num_acoes):  # BubbleSort
    comparacoes, trocas = 0, 0  # contador da questão
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            comparacoes += 1

            if interrompimento:  # segunda etapa
                if comparacoes + trocas == num_acoes:
                    return lista

            if lista[j] > lista[j + 1]:  # trocando os itens no lugar errado
                trocas += 1
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

                if interrompimento:  # segunda etapa
                    if comparacoes + trocas == num_acoes:
                        return lista

    return comparacoes, trocas


def selectionSort(lista, interrompimento, num_acoes):  # SelectionSort
    comparacoes, trocas = 0, 0  # contador da questão
    for i in range(len(lista)):
        minn = i

        for j in range(i + 1, len(lista)):
            comparacoes += 1
            if lista[j] < lista[minn]:
                minn = j

            if interrompimento:  # segunda etapa
                if comparacoes + trocas == num_acoes:
                    return lista

        if i != minn:
            trocas += 1
            lista[i], lista[minn] = lista[minn], lista[i]  # elemento mínimo em cada loop vai para a posição correta

            if interrompimento:  # segunda etapa
                if comparacoes + trocas == num_acoes:
                    return lista

    return comparacoes, trocas


def insertionSort(lista, interrompimento, num_acoes):  # Insertion Sort
    comparacoes, trocas = 0, 0  # contador da questão
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1

        while j >= 0 and key < lista[j]:
            comparacoes += 1

            if interrompimento:  # segunda etapa
                if comparacoes + trocas >= num_acoes:
                    return lista

            trocas += 1
            lista[j + 1] = lista[j]
            j = j - 1

            if interrompimento:  # segunda etapa
                if comparacoes + trocas >= num_acoes:
                    return lista

        lista[j + 1] = key  # elemento (chave) é posto logo após otro elemento menor

        if (j + 1) != 0:  # saiu do loop while pela segunda condição (realiza a comparação)
            comparacoes += 1

            if interrompimento:  # segunda etapa
                if comparacoes + trocas == num_acoes:
                    return lista

    return comparacoes, trocas

def shellSort(lista, interrompimento, num_acoes):  # ShellSort
    comparacoes, trocas = 0, 0
    intervalo = len(lista) // 2
    while intervalo > 0:
        for i in range(intervalo, len(lista)):
            item = lista[i]
            j = i

            while j >= intervalo and lista[j - intervalo] > item:
                comparacoes += 1

                if interrompimento:  # segunda etapa
                    if comparacoes + trocas == num_acoes:
                        return lista

                trocas += 1

                if interrompimento:  # segunda etapa
                    if comparacoes + trocas == num_acoes:
                        return lista

                lista[j] = lista[j - intervalo]
                j -= intervalo

            lista[j] = item

            if j >= intervalo:  # saiu do loop while pela segunda condição (realiza a comparação)
                comparacoes += 1

                if interrompimento:  # segunda etapa
                    if comparacoes + trocas == num_acoes:
                        return lista

        intervalo //= 2

    return comparacoes, trocas

def quickSort(lista):  # QuickSort (Hoare)
    comparacoes, trocas = 0, 0  # contador da questão

    def partition(lista, low, high):  # partição
        nonlocal comparacoes, trocas
        pivot = lista[(high + low) // 2]
        i = low
        j = high
        while True:
            while lista[i] < pivot:
                comparacoes += 1
                i += 1

            while lista[j] > pivot:
                comparacoes += 1
                j -= 1

            if i >= j:
                trocas += 1
                return j

            trocas += 1
            lista[i], lista[j] = lista[j], lista[i]

    def sortHelper(lista, low, high):  # função auxiliar
        if low >= 0 and high >= 0 and low < high:
            nonlocal comparacoes
            p_idx = partition(lista, low, high)
            sortHelper(lista, low, p_idx)
            sortHelper(lista, p_idx + 1, high)

    sortHelper(lista, 0, len(lista) - 1)

    return comparacoes, trocas


# Entrada
livros = input().split(' ')
estagiarios = [['Caça-Rato', 'bubble'], ['Grafite', 'selection'],
               ['Lacraia', 'insertion'], ['Rivaldo', 'shell'], ['Toninho', 'quick']]


# Primeira etapa
count, lessAcoes = 0, 1000000000000000 * 100000000000000
for estagi in estagiarios:
    sort = estagiarios[count][1]
    numeros = [int(num) for num in livros]  # converte lista de strings em lista de inteiros

    if sort == 'bubble':
        acoes = bubbleSort(numeros, False, None)

    elif sort == 'selection':
        acoes = selectionSort(numeros, False, None)

    elif sort == 'insertion':
        acoes = insertionSort(numeros, False, None)

    elif sort == 'shell':
        acoes = shellSort(numeros, False, None)

    else:
        acoes = quickSort(numeros)

    numComp, numTrocas = acoes[0], acoes[1]
    print(f'{estagiarios[count][0]} ordena a lista com {numComp} comparações e '
          f'{numTrocas} trocas.')  # output


    if (numTrocas + numComp) < lessAcoes:  # contagem do número de ações
        lessAcoes = numTrocas + numComp
        vencedor = estagiarios[count][0]
    count += 1

print(f'-VENCEDOR DA RODADA-\nO vencedor da rodada é {vencedor}, com {lessAcoes} ações.')

# Segunda etapa
print(f'-Toninho está a dormir...-\nOs outros estagiários retornam as seguintes listas com essa quantidade'
      f' de ações:')
# lessAcoes = 44
count = 0
for estagi in estagiarios[:4]:
    sort = estagiarios[count][1]
    numeros = [int(num) for num in livros]  # converte lista de strings em lista de inteiros
    if estagiarios[count][0] != vencedor:
        if sort == 'bubble':
            listaInterrompida = bubbleSort(numeros, True, lessAcoes)

        elif sort == 'selection':
            listaInterrompida = selectionSort(numeros, True, lessAcoes)

        elif sort == 'insertion':
            listaInterrompida = insertionSort(numeros, True, lessAcoes)

        elif sort == 'shell':
            listaInterrompida = shellSort(numeros, True, lessAcoes)

        print(f'Com {lessAcoes} ações, {estagiarios[count][0]} ordena a lista assim: {listaInterrompida}')

    count += 1
