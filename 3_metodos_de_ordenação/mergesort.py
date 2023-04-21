# LISTA 3, QUESTÃO FUTURO DO LEÃO
# Funções
def mergeSort(lista):  # MergeSort
    if len(lista) > 1:
        mid = len(lista) // 2  # divied lista ao meio
        esquerda = lista[:mid]
        direita = lista[mid:]
        mergeSort(esquerda)
        mergeSort(direita)

        i = 0
        j = 0
        k = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                lista[k] = esquerda[i]
                i = i + 1

            else:
                lista[k] = direita[j]
                j = j + 1
            k = k + 1

        while i < len(esquerda):
            lista[k] = esquerda[i]
            i = i + 1
            k = k + 1

        while j < len(direita):
            lista[k] = direita[j]
            j = j + 1
            k = k + 1

def getMediana(lista):  # retorna o valor mediano
    if len(lista) % 2 == 0:
        value1 = lista[int((len(lista) / 2) - 1)]
        value2 = lista[int(len(lista) / 2)]
        med = (value1 + value2) / 2

    else:
        med = lista[(len(lista) + 1) / 2]

    return med

# Entradas
sport = input().split(' ')
futuro = input().split(' ')
salarios = sport + futuro
for item in salarios:
    if item == '':
        salarios.remove(item)

valores = [int(valor) for valor in salarios]  # converte lista de strings em lista de inteiros
mergeSort(valores)

# Saída
mediana = getMediana(valores)
print(f'O salário sugerido por Juba na primeira negociação será de {mediana:.2f} mil reais.')  # output
