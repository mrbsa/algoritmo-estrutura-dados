# LISTA 7, QUESTÃO AMOR À CAMISA
# Funções
def setores(num, qtd):
    if num <= 2:  # não é necessário analisar diversas somas
        return max(qtd)

    else:
        table = [qtd[0], max(qtd[0], qtd[1])]  # inicializa a tabela
        for item in range(2, num):
            table = table + [max(table[item - 1], table[item - 2] + qtd[item])]  # insere o a maior soma entre um item da tabela o próximo número não consecutivo da lista

    return table[-1]  # retorna a soma máxima acumulada (último item inserido)

# Entradas e saída
num_setores = int(input())
ocupacao_setor = input().split(' ')
qtd_por_setor = [int(s) for s in ocupacao_setor]  # transforma a entrada de lista de strings em lista de integers

n = setores(num_setores, qtd_por_setor)
print(f'{n} torcedores podem ser fotografados.')  # output
