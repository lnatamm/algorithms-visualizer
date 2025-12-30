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
- Ver os algoritmos funcionando em tempo real
- Ouvir sons baseados nos valores sendo ordenados
- Trocar entre diferentes algoritmos (teclas 1-7)
- Resetar e testar novamente (tecla R)

**Controles:**
- `1` - QuickSort
- `2` - Merge Sort
- `3` - Heap Sort
- `4` - Bubble Sort
- `5` - Insertion Sort
- `6` - Selection Sort
- `7` - Bogo Sort (apenas para arrays pequenos!)
- `SPACE` - Iniciar ordenação
- `R` - Resetar array
- `ESC` - Sair

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

### Teste Rápido no Python:

```python
from sorting import QuickSort, MergeSort

# Array simples
array = [64, 34, 25, 12, 22, 11, 90]
print("Original:", array)

# Ordenar com QuickSort
sorted_array = QuickSort.sort(array.copy())
print("Ordenado:", sorted_array)
```

### Teste Rápido de Performance:

Execute o menu CLI:
```bash
python main.py
```

Escolha opção 8 (Testar TODOS os algoritmos) e use um array de 1000 elementos para ver a diferença de desempenho!

## Dicas

✅ **Para aprender:** Use o visualizador com arrays pequenos (100-500 elementos)

✅ **Para comparar:** Use o menu CLI com arrays médios (1000-10000 elementos)

⚠️ **Evite:** Bogo Sort com mais de 10 elementos (extremamente lento!)

⚠️ **Cuidado:** Bubble/Insertion/Selection Sort são lentos com arrays grandes (>10.000 elementos)

## Recomendações de Tamanho de Array

| Algoritmo | Tamanho Ideal | Máximo Prático |
|-----------|---------------|----------------|
| QuickSort | 1.000 - 1.000.000 | Ilimitado |
| Merge Sort | 1.000 - 1.000.000 | Ilimitado |
| Heap Sort | 1.000 - 1.000.000 | Ilimitado |
| Bubble Sort | 100 - 1.000 | ~10.000 |
| Insertion Sort | 100 - 1.000 | ~10.000 |
| Selection Sort | 100 - 1.000 | ~10.000 |
| Bogo Sort | 5 - 8 | 10 (MÁXIMO!) |

## Personalizando o Visualizador

No arquivo `visualizer.py`, linha final:

```python
# Altere o array_size para ver diferentes comportamentos
visualizer = SortingVisualizer(array_size=100)  # 100, 500, 1000, etc.
```

## Problemas Comuns

**Erro: "No module named pygame"**
```bash
pip install pygame numpy
```

**O visualizador está muito lento**
- Reduza o tamanho do array
- O programa otimiza automaticamente para arrays grandes

**Bogo Sort não termina**
- Isso é normal! Pressione ESC para sair
- Use apenas com arrays de 5-8 elementos

## Próximos Passos

1. ✅ Teste o visualizador com diferentes algoritmos
2. ✅ Compare performance no menu CLI
3. ✅ Leia o código-fonte para entender os algoritmos
4. ✅ Experimente modificar os algoritmos
5. ✅ Adicione seus próprios algoritmos!

## Aprenda Mais

Veja [README.md](README.md) para:
- Explicações detalhadas dos algoritmos
- Análise de complexidade
- Estrutura completa do projeto
