# LISTA 7, QUESTÃO O MEDO DE BEAU
# Funções
def maneiras(n, subgrupo, idx=0):  # n é quantidade de pessoas na audiência
    if sum(subgrupo) == n:  # output
        print(subgrupo)
        return

    for i in range(idx, n):  # idx é um contador de índice em que se começa a
                      # contar para gerar as diferentes instâncias de subgrupos
        count = i + 1  # contador da quantidade de pessoas
        if sum(subgrupo) + count <= n:
            maneiras(n, subgrupo + [count], i)  # recursão (permite as diversas saídas)

# Entrada e chamada da função
audiencia = int(input())

print(f'Uma sessão com {audiencia} pessoas pode ter sua audiência nos seguintes subgrupos:')
maneiras(audiencia, [])
