# Atividade – Capítulo 3: medir o efeito da representação

Solução em Python baseada no capítulo 3 de Teoria dos Grafos.

## Itens essenciais

### 1. Implementações

- `GrafoMatriz`: matriz de adjacência.
- `GrafoLista`: lista de adjacência usando `set`.
- Ambas implementam a interface `Grafo` do material.
- Não foi usado NetworkX.

### 2. Teste do grafo da Figura 3.1

O teste constrói o grafo com:

- `n = 6`
- `m = 8`
- graus ordenados: `(4, 3, 3, 3, 2, 1)`
- soma dos graus: `16 = 2m`
- número de triângulos: `3`

Execute:

```bash
python -m testes.test_grafos
```

### 6. Análise

A matriz de adjacência usa `Theta(n^2)` posições. Já a lista usa `Theta(n+m)`, ou, na contagem pedida na atividade, `n + 2m` posições.

Para `contar_triangulos`, a matriz tem teste de adjacência `Theta(1)`, mas cada chamada de `vizinhos(v)` precisa percorrer uma linha inteira, com custo `Theta(n)`. Na lista, percorrer os vizinhos custa `Theta(d(v))` e, como foi usado `set`, o teste de adjacência é constante em média.

Assim, para grafos esparsos, a lista de adjacência tende a ser mais rápida e muito mais econômica em memória, pois percorre apenas vizinhos existentes. Conforme a densidade cresce, a diferença de espaço diminui assintoticamente e a vantagem da matriz no acesso direto à adjacência pode se tornar mais relevante. Entretanto, nesta implementação específica, a lista também usa `set`, de modo que `tem_aresta` tem custo constante esperado; por isso ela pode continuar competitiva mesmo em densidades maiores.

Se a medição real não seguir exatamente a previsão assintótica, isso pode ocorrer por fatores constantes, implementação de listas e conjuntos do Python, uso de memória/cache e custo de interpretação. Uma forma de testar essa hipótese é repetir as medições, usar a mediana, variar `n` e manter a mesma semente aleatória.

## Benchmark opcional

O arquivo `benchmark.py` implementa os itens 4 e 5 para as três densidades pedidas (`0.001`, `0.05`, `0.5`) com `n = 2000` e três execuções por medição.

```bash
python benchmark.py
```

Observação: a densidade `0.5` com `n = 2000` pode exigir bastante tempo, pois o algoritmo de contagem de triângulos é custoso em grafos densos.
