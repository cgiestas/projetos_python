class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
    
    def adiciona_aresta(self, u, v, peso):
        self.grafo[u-1][v-1] = peso

    def mostra_matriz(self):
        print('A matriz de adjacencias e: ')
        for i in range(self.vertices):
            print(self.grafo[i])

v=int(input('Digite a quantidade de vertices: '))
g=Grafo(v)

a=int(input('Digite a quantidade de arestas: '))
for i in range(a):
    u = int(input('De qual vertice parte esta aresta? '))
    v = int(input('Para qual vertice chega esta aresta? '))
    p = int(input('Qual e o peso desta aresta? '))
    g.adiciona_aresta(u,v,p)

g.mostra_matriz()