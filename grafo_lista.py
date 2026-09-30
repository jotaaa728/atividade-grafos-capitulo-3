class GrafoLista:
    def __init__(self, n):
        self.n = n
        self.lista = [
            set()
            for _ in range(n)
        ]

    def adicionar_aresta(self, u, v):
        self.lista[u].add(v)
        self.lista[v].add(u)

    def sao_adjacentes(self, u, v):
        return v in self.lista[u]
