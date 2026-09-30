import csv
import random
import tracemalloc

from time import perf_counter

from grafo_matriz import GrafoMatriz
from grafo_lista import GrafoLista


def gerar_arestas(n, densidade):
    possiveis = []

    for u in range(n):
        for v in range(u + 1, n):
            possiveis.append((u, v))

    quantidade = round(
        densidade * len(possiveis)
    )

    return random.sample(
        possiveis,
        quantidade
    )


def contar_triangulos(grafo):
    total = 0

    for u in range(grafo.n):
        for v in range(u + 1, grafo.n):

            if not grafo.sao_adjacentes(u, v):
                continue

            for w in range(v + 1, grafo.n):

                if (
                    grafo.sao_adjacentes(u, w)
                    and
                    grafo.sao_adjacentes(v, w)
                ):
                    total += 1

    return total


def construir_grafo(classe, n, arestas):

    tracemalloc.start()

    inicio = perf_counter()

    grafo = classe(n)

    for u, v in arestas:
        grafo.adicionar_aresta(u, v)

    tempo = perf_counter() - inicio

    _, memoria = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    return grafo, tempo, memoria


def executar():
    random.seed(42)

    testes = [
        (50, 0.10),
        (50, 0.50),
        (100, 0.10),
        (100, 0.50),
        (150, 0.10),
        (150, 0.50),
    ]

    resultados = []

    for n, densidade in testes:

        arestas = gerar_arestas(
            n,
            densidade
        )

        for classe in [
            GrafoMatriz,
            GrafoLista
        ]:

            grafo, tempo_construcao, memoria = (
                construir_grafo(
                    classe,
                    n,
                    arestas
                )
            )

            inicio = perf_counter()

            triangulos = contar_triangulos(
                grafo
            )

            tempo_triangulos = (
                perf_counter() - inicio
            )

            resultado = {
                "representacao":
                    classe.__name__,

                "vertices":
                    n,

                "arestas":
                    len(arestas),

                "densidade":
                    densidade,

                "tempo_construcao":
                    tempo_construcao,

                "tempo_triangulos":
                    tempo_triangulos,

                "memoria_bytes":
                    memoria,

                "triangulos":
                    triangulos
            }

            resultados.append(resultado)

            print(
                classe.__name__,
                "| vertices:", n,
                "| densidade:", densidade,
                "| arestas:", len(arestas),
                "| triangulos:", triangulos,
                "| tempo:",
                round(
                    tempo_triangulos,
                    6
                ),
                "s",
                "| memoria:",
                round(
                    memoria / 1024,
                    2
                ),
                "KB"
            )

        print()

    with open(
        "resultados.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.DictWriter(
            arquivo,
            fieldnames=resultados[0].keys()
        )

        escritor.writeheader()

        escritor.writerows(
            resultados
        )


if __name__ == "__main__":
    executar()
