import random
import statistics
import time

from grafo.lista import GrafoLista
from grafo.matriz import GrafoMatriz
from grafo.triangulos import contar_triangulos


def gerar_arestas(n: int, densidade: float, semente: int = 42):
    random.seed(semente)
    arestas = []
    for u in range(n):
        for v in range(u + 1, n):
            if random.random() < densidade:
                arestas.append((u, v))
    return arestas


def construir(cls, n, arestas):
    g = cls(n)
    for u, v in arestas:
        g.inserir_aresta(u, v)
    return g


def medir(g, repeticoes=3):
    tempos = []
    resultado = None
    for _ in range(repeticoes):
        inicio = time.perf_counter()
        resultado = contar_triangulos(g)
        tempos.append(time.perf_counter() - inicio)
    return statistics.median(tempos), resultado


def espaco_posicoes(g, tipo: str):
    n = g.ordem()
    m = g.tamanho()
    return n * n if tipo == "matriz" else n + 2 * m


def main():
    n = 2000
    densidades = [0.001, 0.05, 0.5]

    print("densidade,implementacao,n,m,triangulos,tempo_mediano_s,espaco_posicoes")

    for densidade in densidades:
        arestas = gerar_arestas(n, densidade)

        for nome, cls in [("matriz", GrafoMatriz), ("lista", GrafoLista)]:
            g = construir(cls, n, arestas)
            tempo, triangulos = medir(g, 3)
            espaco = espaco_posicoes(g, nome)
            print(
                f"{densidade},{nome},{g.ordem()},{g.tamanho()},"
                f"{triangulos},{tempo:.6f},{espaco}"
            )


if __name__ == "__main__":
    main()
