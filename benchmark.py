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


def medir(g, repeticoes=3, nome="grafo"):
    tempos = []
    resultado = None

    for repeticao in range(1, repeticoes + 1):
        print(f"    Execução {repeticao}/{repeticoes} de {nome}...", flush=True)

        inicio = time.perf_counter()
        resultado = contar_triangulos(g)
        tempo = time.perf_counter() - inicio

        tempos.append(tempo)

        print(f"      Tempo: {tempo:.6f} s", flush=True)

    return statistics.median(tempos), resultado


def espaco_posicoes(g, tipo: str):
    n = g.ordem()
    m = g.tamanho()
    return n * n if tipo == "matriz" else n + 2 * m


def main():
    n = 2000
    densidades = [0.001, 0.05, 0.5]

    resultados = []

    print("=" * 70)
    print("ATIVIDADE - MEDIR O EFEITO DA REPRESENTAÇÃO")
    print(f"n = {n}")
    print("=" * 70)

    for indice, densidade in enumerate(densidades, start=1):
        print()
        print(f"[{indice}/{len(densidades)}] Gerando grafo com densidade {densidade}...")
        print("    Isso pode levar alguns instantes.", flush=True)

        inicio_geracao = time.perf_counter()
        arestas = gerar_arestas(n, densidade)
        tempo_geracao = time.perf_counter() - inicio_geracao

        print(
            f"    Grafo gerado: {len(arestas)} arestas "
            f"({tempo_geracao:.6f} s)",
            flush=True,
        )

        for nome, cls in [("matriz", GrafoMatriz), ("lista", GrafoLista)]:
            print()
            print(f"  Testando implementação: {nome.upper()}")

            inicio_construcao = time.perf_counter()
            g = construir(cls, n, arestas)
            tempo_construcao = time.perf_counter() - inicio_construcao

            print(
                f"    Estrutura construída em {tempo_construcao:.6f} s",
                flush=True,
            )
            print("    Iniciando contagem de triângulos...", flush=True)

            tempo, triangulos = medir(
                g,
                repeticoes=3,
                nome=f"{nome} (densidade {densidade})",
            )

            espaco = espaco_posicoes(g, nome)

            resultados.append(
                (
                    densidade,
                    nome,
                    g.ordem(),
                    g.tamanho(),
                    triangulos,
                    tempo,
                    espaco,
                )
            )

            print(
                f"    Concluído: {triangulos} triângulos | "
                f"mediana = {tempo:.6f} s | "
                f"espaço = {espaco} posições",
                flush=True,
            )

    print()
    print("=" * 70)
    print("RESULTADOS FINAIS")
    print("=" * 70)
    print(
        "densidade,implementacao,n,m,triangulos,"
        "tempo_mediano_s,espaco_posicoes"
    )

    for densidade, nome, ordem, tamanho, triangulos, tempo, espaco in resultados:
        print(
            f"{densidade},{nome},{ordem},{tamanho},"
            f"{triangulos},{tempo:.6f},{espaco}"
        )


if __name__ == "__main__":
    main()
