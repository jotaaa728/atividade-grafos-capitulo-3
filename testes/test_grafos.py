from grafo.lista import GrafoLista
from grafo.matriz import GrafoMatriz
from grafo.triangulos import contar_triangulos

ARESTAS = [
    (0, 1), (0, 2), (1, 2), (1, 3),
    (2, 3), (2, 4), (3, 4), (4, 5)
]


def construir(cls):
    g = cls(6)
    for u, v in ARESTAS:
        g.inserir_aresta(u, v)
    return g


def conferir(g):
    assert g.ordem() == 6
    assert g.tamanho() == 8

    graus = sorted((g.grau(v) for v in g.vertices()), reverse=True)
    assert graus == [4, 3, 3, 3, 2, 1]

    soma_graus = sum(g.grau(v) for v in g.vertices())
    assert soma_graus == 2 * g.tamanho() == 16

    assert contar_triangulos(g) == 3


def test_grafo_matriz():
    conferir(construir(GrafoMatriz))


def test_grafo_lista():
    conferir(construir(GrafoLista))


if __name__ == "__main__":
    test_grafo_matriz()
    test_grafo_lista()
    print("Todos os testes passaram.")
