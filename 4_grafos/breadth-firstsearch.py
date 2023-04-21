# LISTA 5, QUESTÃO TURBINANDO PUBLICAÇÕES
# Classes e métodos
class Graph(object):  # grafo
    def __init__(self):  # método construtor
        self.adj = {}

    def createGraph(self, size):  # cria o grafo com a quantidade de arestas informadas
        for num in range(0, size):
            self.adj[num] = []

    def newEdge(self, u, v):  # adiciona arestas entre os vértices u e v ao grafo
        self.adj[u].append(v)

  # Busca em largura
    def bfs(self, node, size):  # breadth-first search
        marcado = {}  # nós percorridos
        queue = [node]  # fila

        while len(marcado) != size:  # limita a lista apenas aos seguidores alcançados
            u = queue.pop(0)  # nó

            if u not in marcado:
                if u != node:  # não adiciona o nó em que se realiza a bfs na lista
                    marcado[u] = True

                for v in self.adj[u]:  # nó seguinte
                    queue.append(v)

        return marcado

# Entradas
numUsers = int(input())
userId = int(input())
boostPrice = int(input())

userRange = int(boostPrice // 5.25)  # quantidade de usuários atingidos além de seus seguidores

# Operações do grafo
g = Graph()  # cria o grafo
g.createGraph(numUsers)

while numUsers > 0:
  seguidores = input().split(' ')
  seguidores.remove(':')
  followers = [int(num) for num in seguidores]

  for n in followers[1::]:
    g.newEdge(followers[0], n)  # insere novas arestas no grafo

  numUsers -= 1

nodos = g.bfs(userId, len(g.adj[userId]) + userRange)  # len + range = até a qtd de nodos a que vai a bfs

# Saída
nodes = [str(nodo) for nodo in nodos]  # formatação
print(nodes)  # output
