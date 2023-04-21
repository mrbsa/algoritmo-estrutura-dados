# LISTA 1, QUESTÃO O ANTI-SISTEMA DE ED. FÍSICA
# Funções independentes
def pilhaImaculada(pilha):  # checa a ordem da atual pilha
    days = []
    hours = []

    for i in pilha:  # separa os dias das horas para avaliar cada um
        item = list(i)
        day = item[0:2]
        hour = item[2::]

        hours.append(hour)
        days.append(day)

    count = 1
    correct = True

    for j in days:  # avalia os dias da semana
        if count < len(days):

            if j < days[count]:
                count += 1

            elif j == days[count]:  # avalia as horas
                idx = days.index(j)  # index

                if hours[idx] <= hours[count]:
                    count += 1

                else:
                    correct = False

            else:
                correct = False
                break

    return correct


def novaLocacao(pilha, codigo):
    code = list(codigo)
    day_code = code[0:2]
    hour_code = code[2::]

    days = []
    hours = []

    for i in pilha:  # separa dias e horários
        item = list(i)
        day = item[0:2]
        hour = item[2::]

        hours.append(hour)
        days.append(day)

    idx = 0  # index

    for j in days:  # localiza o dia
        if day_code > j:
            idx += 1

        elif day_code == j:  # localiza as horas
            if hour_code > hours[idx]:
                idx += 1

            else:
                break

        else:
            break

    pilha.insert(idx, codigo)

    return pilha


# Corpo
solicitacoes = input().split(',')
codigo_novo = input(str())

# Output
ordem = pilhaImaculada(solicitacoes)
if not ordem:
    print('A pilha está um caos.')
else:
    print(novaLocacao(solicitacoes, codigo_novo))
