class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0]*self.vertices for i in range(self.vertices)]
    
    def adiciona_aresta(self, u, v):
        self.grafo[u-1][v-1] = 1 #para grafo direcionado simples
        #trocar = por += se for grafo multiplo (não simples)
        #self.grafo[v-1][u-1] = 1 caso o grafo não seja direcionado

    def mostra_matriz(self):
        print('A matriz de adjacencias e: ')
        for i in range(self.vertices):
            print(self.grafo[i])

g = Grafo(4)

g.adiciona_aresta(1,2)
g.adiciona_aresta(3,4)
g.adiciona_aresta(2,3)

g.mostra_matriz()