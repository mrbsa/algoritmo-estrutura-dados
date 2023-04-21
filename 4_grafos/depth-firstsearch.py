# LISTA 5, QUESTÃO MIM DÊ PAPAI 
# Classes e métodos
class Graph(object):  # grafo
    def __init__(self):  # método construtor
        self.adj = {}

    def createGraph(self, size):  # cria o grafo com a quantidade de arestas informadas
        for num in range(1, size + 1):
            self.adj[num] = []

    def newEdge(self, u, v):  # adiciona arestas entre os vértices u e v ao grafo
        self.adj[u].append(v)
        self.adj[v].append(u)  # grafo não direcionado

    # Busca em profundidade
    def dfs(self, node):  # depth-first search
        marcado = {}  # nós percorridos
        stack = [node]  # pilha

        while stack:
            u = stack.pop()  # nó

            if u not in marcado:
                marcado[u] = True

                for v in self.adj[u]:  # nó seguinte
                    stack.append(v)

        return len(marcado)

# Entradas
values = input().split(' ')
valores = [int(val) for val in values]
usuarios, conexoes = valores[0], valores[1]

# Operações do Grafo
g = Graph()  # cria o grafo
g.createGraph(usuarios)

while conexoes > 0:
  amizades = input().split(' ')
  nos = [int(no) for no in amizades]
  g.newEdge(nos[0], nos[1])  # insere as conexões no grafo
  conexoes -= 1

# Saídas
noticia = []
for node in g.adj:
    noticia.append(g.dfs(node))
    
formNoticia = " ".join(str(num) for num in noticia)
print(formNoticia)  # output
