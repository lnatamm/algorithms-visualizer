# 🚀 Guia de Início Rápido

## Instalação

1. **Clone ou baixe o projeto**

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

## Modos de Uso

### 🎮 Modo 1: Visualizador Gráfico (Recomendado)

```bash
python visualizer.py
```

**O que você pode fazer:**
- ✨ **3 Categorias**: Ordenação, Busca em Arrays e Busca em Grafos
- 🎯 **18 Algoritmos**: 7 de ordenação, 5 de busca, 6 de grafos
- 👀 Ver os algoritmos funcionando em tempo real
- 🔊 Ouvir sons baseados nos valores (ordenação/busca)
- 🌐 Visualizar grafos com destaque de caminhos

**Fluxo de Uso:**
1. Clique em **"Iniciar"**
2. Escolha o tipo: **Ordenação**, **Busca** ou **Grafos**
3. Configure:
   - Ordenação/Busca: Digite o tamanho do array (1-10000)
   - Grafos: Escolha entre **Globais** ou **Locais**
4. Selecione o algoritmo desejado
5. Observe a mágica acontecer! ✨

**Controles:**
- `ESC` - Voltar ao menu anterior
- Mouse - Clicar em botões e digitar valores

### 📊 Modo 2: Menu de Testes CLI

```bash
python main.py
```

**O que você pode fazer:**
- Testar algoritmos individualmente
- Comparar TODOS os algoritmos de uma vez
- Escolher o tamanho do array
- Ver métricas de tempo e ranking de desempenho

### 📝 Modo 3: Exemplos de Código

```bash
python exemplos.py
```

Veja exemplos práticos de como usar cada algoritmo em seu próprio código.

## Primeiro Teste

### Teste Rápido - Visualizador:

1. Execute `python visualizer.py`
2. Clique em **"Iniciar"**
3. Escolha **"Ordenação"**
4. Digite **100** para o tamanho
5. Selecione **"QuickSort"**
6. Veja a mágica! 🎨

### Teste Rápido - Busca em Arrays:

1. Execute `python visualizer.py`
2. Clique em **"Iniciar"**
3. Escolha **"Busca"**
4. Digite **500** para o tamanho
5. Selecione **"Binary Search"**
6. Veja a busca binária em ação! 🔍

### Teste Rápido - Grafos:

1. Execute `python visualizer.py`
2. Clique em **"Iniciar"**
3. Escolha **"Grafos"**
4. Selecione **"Globais"**
5. Escolha **"Dijkstra"**
6. Veja o caminho mais curto sendo calculado! 🌐

### Teste Rápido de Performance:

Execute o menu CLI:
```bash
python main.py
```

Escolha opção 8 (Testar TODOS os algoritmos) e use um array de 1000 elementos para ver a diferença de desempenho!

## Dicas

### Ordenação
✅ **Para aprender:** Use arrays pequenos (100-500 elementos)
✅ **Para comparar:** Use arrays médios (1000-5000 elementos)
⚠️ **Evite:** Bogo Sort com mais de 10 elementos!

### Busca em Arrays
✅ **Linear Search:** Funciona com qualquer tamanho
✅ **Binary Search:** Muito rápido, veja a diferença!
✅ **Jump Search:** Interessante para tamanhos médios (500-2000)

### Grafos
✅ **Algoritmos Globais:** Dijkstra, Bellman-Ford, Floyd-Warshall
   - Encontram o caminho mais curto considerando pesos
   - Dijkstra é o mais rápido (mas não aceita pesos negativos)
   
✅ **Algoritmos Locais:** BFS, DFS, A*
   - BFS encontra o caminho com menos arestas
   - DFS explora profundamente
   - A* usa heurística para otimizar

## Recomendações de Tamanho

### Arrays (Ordenação/Busca)

| Algoritmo | Tamanho Ideal | Máximo Prático |
|-----------|---------------|----------------|
| QuickSort | 1.000 - 10.000 | 10.000 |
| Merge Sort | 1.000 - 10.000 | 10.000 |
| Heap Sort | 1.000 - 10.000 | 10.000 |
| Bubble Sort | 100 - 500 | 1.000 |
| Insertion Sort | 100 - 500 | 1.000 |
| Selection Sort | 100 - 500 | 1.000 |
| Bogo Sort | 5 - 8 | 10 (MÁXIMO!) |
| Linear Search | 100 - 1.000 | 10.000 |
| Binary Search | 500 - 10.000 | 10.000 |
| Interpolation Search | 500 - 5.000 | 10.000 |
| Jump Search | 500 - 5.000 | 10.000 |
| Exponential Search | 500 - 5.000 | 10.000 |

### Grafos

- **Número de Nós:** 10 (fixo na versão atual)
- **Algoritmos Rápidos:** Dijkstra, BFS, DFS, A*
- **Algoritmos Lentos:** Floyd-Warshall (O(V³))
| Insertion Sort | 100 - 1.000 | ~10.000 |
| Selection Sort | 100 - 1.000 | ~10.000 |
| Bogo Sort | 5 - 8 | 10 (MÁXIMO!) |

## Problemas Comuns

**Erro: "No module named pygame"**
```bash
pip install pygame numpy
```

**O visualizador está muito lento**
- Reduza o tamanho do array
- Use algoritmos mais rápidos (QuickSort, Merge Sort, Binary Search)

**Bogo Sort não termina**
- Isso é normal! Pressione ESC para sair
- Use apenas com arrays de 5-8 elementos

**Algoritmo de busca não encontra o elemento**
- Certifique-se de que está usando array ordenado para Binary/Interpolation/Jump/Exponential Search
- O target é escolhido aleatoriamente do próprio array, então sempre será encontrado

**Grafos não mostram caminho**
- Verifique se o algoritmo terminou de executar
- O caminho é destacado em verde/dourado ao final

## Personalizando

### Alterar número de nós no grafo
No arquivo [visualizer.py](visualizer.py), método `setup_graph()`:
```python
self.node_count = 15  # Altere de 10 para 15, por exemplo
```

### Alterar velocidade de visualização
Em cada método visual, altere o FPS:
```python
self.clock.tick(120)  # Mais rápido (era 60)
self.clock.tick(30)   # Mais lento (era 60)
```

## Próximos Passos

1. ✅ Teste o visualizador com **todos os 3 tipos** de algoritmos
2. ✅ Compare diferentes algoritmos de ordenação
3. ✅ Veja a diferença entre Linear e Binary Search
4. ✅ Explore algoritmos de grafos (Dijkstra vs BFS vs A*)
5. ✅ Leia [DOCUMENTACAO_TECNICA.md](DOCUMENTACAO_TECNICA.md) para detalhes de implementação
6. ✅ Experimente modificar os algoritmos
7. ✅ Adicione seus próprios algoritmos!

## Aprenda Mais

📖 **Documentação Completa:**
- [README.md](README.md) - Visão geral e complexidades
- [DOCUMENTACAO_TECNICA.md](DOCUMENTACAO_TECNICA.md) - Arquitetura e implementação
- [ESTRUTURA.md](ESTRUTURA.md) - Estrutura de arquivos do projeto
