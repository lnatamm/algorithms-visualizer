# 🎯 Visualizador de Algoritmos de Ordenação
## DISCLAIMER: Utilizado o modelo de I.A Claude Sonnet 4.5 para a geração da interface gráfica


Um projeto interativo para visualizar e comparar diferentes algoritmos de ordenação em Python com Pygame.

## 📋 Algoritmos Implementados

1. **QuickSort** - Divisão e conquista eficiente
2. **Merge Sort** - Divisão e conquista estável
3. **Heap Sort** - Ordenação usando heap
4. **Bubble Sort** - Algoritmo simples de comparação
5. **Insertion Sort** - Construção incremental
6. **Selection Sort** - Seleção do menor elemento
7. **Bogo Sort** - Algoritmo aleatório (MUITO INEFICIENTE!)

## 🚀 Como Usar

### Visualizador Gráfico

Execute o visualizador para ver os algoritmos em ação:

```bash
python visualizer.py
```

**Controles:**
- `SPACE` - Iniciar ordenação
- `R` - Resetar array
- `ESC` - Sair
- `1-7` - Selecionar algoritmo

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
- ✅ Visualização em tempo real das operações
- ✅ Sons correspondentes aos valores dos elementos
- ✅ Destaque de comparações e trocas
- ✅ Contador de operações
- ✅ Suporte para arrays grandes (otimização automática)
- ✅ Seleção de algoritmo em tempo real

### Menu CLI
- ✅ Teste individual de algoritmos
- ✅ Comparação de todos os algoritmos
- ✅ Medição de tempo de execução
- ✅ Verificação de correção
- ✅ Ranking de desempenho

## ⚠️ Avisos

- **Bogo Sort**: Não use com arrays grandes (>10 elementos). É extremamente ineficiente!
- **Bubble/Insertion/Selection Sort**: Lentos para arrays muito grandes (>10.000 elementos)

## 📊 Complexidade dos Algoritmos

| Algoritmo | Melhor Caso | Caso Médio | Pior Caso | Espaço |
|-----------|-------------|------------|-----------|---------|
| QuickSort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Bogo Sort | O(n) | O(n·n!) | O(∞) | O(1) |

## 🎨 Cores no Visualizador

- 🔵 **Azul**: Elementos não processados
- 🟡 **Amarelo**: Elementos sendo comparados
- 🔴 **Vermelho**: Elementos sendo trocados
- 🟢 **Verde**: Elementos ordenados

## 🤝 Contribuindo

Sinta-se à vontade para adicionar novos algoritmos ou melhorar os existentes!

## 📝 Licença

Este projeto é livre para uso educacional.
