# LISTA 1, QUESTÃO BALAÕ NET
# Classes e métodos
class DoubleNode:  # Nó duplo
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoubleList:  # Lista Duplamente Encadeada
    def __init__(self):  # método autoconstrutor
        self.head = None
        self.tail = None

    def push(self, data):  # adição (no fim da lista)
        new_node = DoubleNode(data)
        new_node.next = None

        if self.head == None:
            new_node.previous = None
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node
        new_node.previous = last_node
        return

    def pop(self):  # remove itens do final
        if self.head.next == None:
            self.head = None
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.previous.next = None


    def remove(self, x):  # remoção (do elemento x)
        if self.head.next == None:
            if self.head.item == x:
                self.head = None
            return

        if self.head.data == x:
            self.head = self.head.next
            self.head.previous = None
            return

        current_node = self.head
        while current_node.next != None:
            if current_node.data == x:
                break
            current_node = current_node.next

        if current_node.next != None:
            current_node.previous.next = current_node.next
            current_node.next.previous = current_node.previous

        else:
            if current_node.data == x:
                current_node.previous.next = None


    def insert(self, x):  # insere elemento x no início
        if self.head == None:
            new_node = DoubleNode(x)
            self.head = new_node
            return

        new_node = DoubleNode(x)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node


    def display(self):  # exibição do histórico
        contents = self.head

        while contents:
            print(contents.data)
            contents = contents.next

    def reverse(self):  # inverte a lista
        current_node = self.head
        new_node = current_node.next
        current_node.next = None
        current_node.previous = new_node

        while new_node  != None:
            new_node .previous = new_node .next
            new_node .next = current_node
            current_node = new_node
            new_node = new_node .previous

        self.head = current_node


    def listing(self):  # converte em lista
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data

    def length(self):  # tamanho da lista
        if self.head == None:
            return 0
        current_node = self.head
        total = 0
        while current_node:
            total += 1
            current_node = current_node.next
        return total


# Funções
def dataFinder(x, y):  # separa o comando da informação
    lista = x.split(' ')
    if y == 'comando':
        return lista[0]
    else:
        return lista[1]

# Input
entrada = input()
historico_de_pesquisa = DoubleList()

count = 0

if entrada == 'END':
    pass
else:
    while entrada != 'END':

        if entrada == 'EXIB':
            if count == 0:
                historico_de_pesquisa.reverse()
                historico_de_pesquisa.display()

            else:  # display da lista fica ao contrário, com exceção do método FIND
                lista_historico = historico_de_pesquisa.listing()
                stack = DoubleList()

                for item in lista_historico[count::]:  # separa os items do FIND
                    stack.push(item)
                stack.reverse()

                while historico_de_pesquisa.length() > count:  # inverte o restante
                    historico_de_pesquisa.pop()
                historico_de_pesquisa.reverse()
                lista_find = historico_de_pesquisa.listing()

                for item in lista_find:
                    stack.insert(item)

                stack.display()

        else:
            comando = dataFinder(entrada, 'comando')
            pagina_web = dataFinder(entrada, 'web')

            if comando == 'REM':
                historico_de_pesquisa.remove(pagina_web)
                
            elif comando == 'ADD':
                historico_de_pesquisa.push(pagina_web)
                
            elif comando == 'FIND':
                historico_de_pesquisa.remove(pagina_web)
                historico_de_pesquisa.insert(pagina_web)

                count += 1

        entrada = input()
