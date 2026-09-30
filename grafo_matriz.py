class GrafoMatriz:
    def __init__(self, n):
        self.n = n
        self.matriz = [
            [False] * n
            for _ in range(n)
        ]

    def adicionar_aresta(self, u, v):
        self.matriz[u][v] = True
        self.matriz[v][u] = True

    def sao_adjacentes(self, u, v):
        return self.matriz[u][v]
