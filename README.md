# 🎯 Visualizador de Algoritmos
## DISCLAIMER: Utilizado o modelo de I.A Claude Sonnet 4.5 para a geração da interface gráfica

Um projeto interativo para visualizar e comparar diferentes algoritmos de ordenação, busca e grafos em Python com Pygame.

## 📋 Algoritmos Implementados

### 🔄 Algoritmos de Ordenação (7)
1. **QuickSort** - Divisão e conquista eficiente
2. **Merge Sort** - Divisão e conquista estável
3. **Heap Sort** - Ordenação usando heap
4. **Bubble Sort** - Algoritmo simples de comparação
5. **Insertion Sort** - Construção incremental
6. **Selection Sort** - Seleção do menor elemento
7. **Bogo Sort** - Algoritmo aleatório (MUITO INEFICIENTE!)

### 🔍 Algoritmos de Busca em Arrays (5)
1. **Linear Search** - Busca sequencial simples
2. **Binary Search** - Busca binária em array ordenado
3. **Interpolation Search** - Busca por interpolação
4. **Jump Search** - Busca por saltos
5. **Exponential Search** - Busca exponencial

### 🌐 Algoritmos de Busca em Grafos (6)

#### Algoritmos Globais (3)
1. **Dijkstra** - Caminho mais curto (sem pesos negativos)
2. **Bellman-Ford** - Caminho mais curto (aceita pesos negativos)
3. **Floyd-Warshall** - Todos os caminhos mais curtos

#### Algoritmos Locais (3)
1. **BFS (Breadth-First Search)** - Busca em largura
2. **DFS (Depth-First Search)** - Busca em profundidade
3. **A*** - Busca heurística com função de custo

## 🚀 Como Usar

### Visualizador Gráfico Interativo

Execute o visualizador para ver os algoritmos em ação:

```bash
python visualizer.py
```

**Fluxo de Navegação:**
1. **Menu Inicial** - Clique em "Iniciar"
2. **Escolha o Tipo** - Selecione entre Ordenação, Busca ou Grafos
3. **Configuração**:
   - **Ordenação/Busca**: Insira o tamanho do array (1-10000)
   - **Grafos**: Escolha entre algoritmos Globais ou Locais
4. **Seleção de Algoritmo** - Escolha o algoritmo desejado
5. **Visualização** - Observe o algoritmo em ação!

**Controles Gerais:**
- `ESC` - Voltar ao menu anterior
- Mouse - Interação com botões e campos de entrada

### Menu de Testes (CLI)

Execute o menu de linha de comando para testar e comparar algoritmos:

```bash
python main.py
```

O menu permite:
- Testar algoritmos individualmente
- Comparar todos os algoritmos
- Escolher o tamanho do array
- Ver ranking de desempenho

## 📦 Instalação

### Requisitos

- Python 3.7+
- Pygame
- NumPy

### Instalar dependências

```bash
pip install -r requirements.txt
```

## ⚙️ Estrutura do Projeto

```
sorting-algorithms/
│
├── sorting/
│   ├── __init__.py
│   ├── quicksort.py
│   ├── mergesort.py
│   ├── heapsort.py
│   ├── bubblesort.py
│   ├── insertionsort.py
│   ├── selectionsort.py
│   └── bogosort.py
│
├── main.py          # Menu CLI de testes
├── visualizer.py    # Visualizador gráfico
├── requirements.txt
└── README.md
```

## 🎮 Funcionalidades

### Visualizador
- ✅ **3 Categorias de Algoritmos**: Ordenação, Busca e Grafos
- ✅ **18 Algoritmos Diferentes**: 7 de ordenação, 5 de busca, 6 de grafos
- ✅ Visualização em tempo real das operações
- ✅ Sons correspondentes aos valores dos elementos (ordenação/busca)
- ✅ Destaque de comparações, trocas e caminhos
- ✅ Contador de operações
- ✅ Suporte para arrays grandes (1-10.000 elementos)
- ✅ Interface interativa com sistema de navegação por menus
- ✅ **Visualização de Grafos**:
  - Layout circular com 10 nós
  - Arestas bidirecionais com pesos
  - Destaque do caminho mais curto em verde
  - Visualização passo a passo do algoritmo

### Menu CLI
- ✅ Teste individual de algoritmos
- ✅ Comparação de todos os algoritmos
- ✅ Medição de tempo de execução
- ✅ Verificação de correção
- ✅ Ranking de desempenho

## ⚠️ Avisos

### Algoritmos de Ordenação
- **Bogo Sort**: Não use com arrays grandes (>10 elementos). É extremamente ineficiente!
- **Bubble/Insertion/Selection Sort**: Lentos para arrays muito grandes (>10.000 elementos)

### Algoritmos de Busca
- **Binary/Interpolation/Jump/Exponential Search**: Requerem array ordenado
- **Linear Search**: Funciona em qualquer array, mas é lento para arrays grandes

### Algoritmos de Grafos
- **Dijkstra**: Não funciona corretamente com pesos negativos
- **Floyd-Warshall**: Pode ser lento para grafos muito grandes (O(V³))
- **A***: A qualidade do resultado depende da função heurística

## 📊 Complexidade dos Algoritmos

### Algoritmos de Ordenação

| Algoritmo | Melhor Caso | Caso Médio | Pior Caso | Espaço |
|-----------|-------------|------------|-----------|---------|
| QuickSort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Bogo Sort | O(n) | O(n·n!) | O(∞) | O(1) |

### Algoritmos de Busca em Arrays

| Algoritmo | Pré-requisito | Complexidade | Espaço |
|-----------|---------------|--------------|---------|
| Linear Search | - | O(n) | O(1) |
| Binary Search | Array ordenado | O(log n) | O(1) |
| Interpolation Search | Array ordenado uniformemente | O(log log n) / O(n) | O(1) |
| Jump Search | Array ordenado | O(√n) | O(1) |
| Exponential Search | Array ordenado | O(log n) | O(1) |

### Algoritmos de Grafos

| Algoritmo | Tipo | Complexidade | Características |
|-----------|------|--------------|-----------------|
| Dijkstra | Global | O((V+E) log V) | Caminho mais curto, sem pesos negativos |
| Bellman-Ford | Global | O(V·E) | Detecta ciclos negativos |
| Floyd-Warshall | Global | O(V³) | Todos os pares de caminhos |
| BFS | Local | O(V+E) | Caminho mais curto (sem pesos) |
| DFS | Local | O(V+E) | Exploração em profundidade |
| A* | Local | O(b^d) | Busca heurística otimizada |

*V = número de vértices, E = número de arestas, b = fator de ramificação, d = profundidade*

## 🎨 Cores no Visualizador

### Ordenação e Busca em Arrays
- 🔵 **Azul**: Elementos não processados
- 🟡 **Amarelo**: Elementos sendo comparados
- 🔴 **Vermelho**: Elementos sendo trocados/pivô
- 🟢 **Verde**: Elementos ordenados ou alvo encontrado
- 🟠 **Laranja**: Elemento atual na busca

### Grafos
- 🔵 **Azul**: Nó inicial
- 🔴 **Vermelho**: Nó final/alvo
- 🟡 **Amarelo**: Nó sendo processado
- 🟢 **Verde**: Nós visitados e caminho final
- 🟠 **Dourado (Arestas)**: Caminho mais curto destacado
- ⚪ **Branco (Texto)**: Rótulos de nós e pesos de arestas

## 🤝 Contribuindo

Sinta-se à vontade para adicionar novos algoritmos ou melhorar os existentes!

## 📝 Licença

Este projeto é livre para uso educacional.
