# 📁 Estrutura do Projeto

```
sorting-algorithms/
│
├── 📂 sorting/                    # Módulo com todos os algoritmos
│   ├── __init__.py               # Inicialização do módulo
│   ├── quicksort.py              # QuickSort - O(n log n) médio
│   ├── mergesort.py              # Merge Sort - O(n log n) garantido
│   ├── heapsort.py               # Heap Sort - O(n log n) garantido
│   ├── bubblesort.py             # Bubble Sort - O(n²)
│   ├── insertionsort.py          # Insertion Sort - O(n²)
│   ├── selectionsort.py          # Selection Sort - O(n²)
│   └── bogosort.py               # Bogo Sort - O(n·n!) - NÃO USE!
│
├── 🎮 visualizer.py              # Visualizador gráfico interativo
├── 📊 main.py                    # Menu CLI para testes e comparações
├── 📝 exemplos.py                # Exemplos de uso dos algoritmos
├── ✅ test_sorting.py            # Testes de correção
│
├── 📖 README.md                  # Documentação completa
├── 🚀 QUICKSTART.md              # Guia de início rápido
├── 📋 requirements.txt           # Dependências do projeto
└── 📄 ESTRUTURA.md               # Este arquivo
```

## 🎯 Arquivos Principais

### Execução

1. **visualizer.py** - Para visualização gráfica
   ```bash
   python visualizer.py
   ```
   - Interface gráfica com Pygame
   - Visualização em tempo real
   - Sons correspondentes aos valores
   - Seleção de algoritmo interativa

2. **main.py** - Para testes e benchmarks
   ```bash
   python main.py
   ```
   - Menu interativo
   - Testes individuais ou comparativos
   - Medição de performance
   - Ranking de algoritmos

3. **exemplos.py** - Para ver exemplos de código
   ```bash
   python exemplos.py
   ```
   - Uso básico de cada algoritmo
   - Comparação de performance
   - Diferentes casos de teste

4. **test_sorting.py** - Para validar correção
   ```bash
   python test_sorting.py
   ```
   - Testes automatizados
   - Validação de todos os algoritmos
   - Casos extremos e especiais

### Documentação

- **README.md** - Documentação completa do projeto
- **QUICKSTART.md** - Guia rápido para começar
- **ESTRUTURA.md** - Visão geral da estrutura (este arquivo)

### Configuração

- **requirements.txt** - Lista de dependências Python
  ```
  pygame
  numpy
  ```

## 🔧 Módulo sorting/

Cada arquivo contém uma classe com método estático `sort()`:

```python
from sorting import QuickSort

array = [5, 2, 8, 1, 9]
sorted_array = QuickSort.sort(array)
```

### Algoritmos Disponíveis

| Arquivo | Classe | Complexidade | Uso Recomendado |
|---------|--------|--------------|-----------------|
| quicksort.py | QuickSort | O(n log n) | Uso geral, arrays grandes |
| mergesort.py | MergeSort | O(n log n) | Arrays grandes, estabilidade |
| heapsort.py | HeapSort | O(n log n) | Arrays grandes, sem espaço extra |
| bubblesort.py | BubbleSort | O(n²) | Arrays pequenos, didático |
| insertionsort.py | InsertionSort | O(n²) | Arrays pequenos/quase ordenados |
| selectionsort.py | SelectionSort | O(n²) | Arrays pequenos, didático |
| bogosort.py | BogoSort | O(∞) | NUNCA USE (apenas didático!) |

## 🎨 Características

### visualizer.py
- ✅ Visualização em tempo real
- ✅ Cores indicativas (azul/amarelo/vermelho/verde)
- ✅ Sons baseados nos valores
- ✅ Contador de operações
- ✅ Otimização automática para arrays grandes
- ✅ 7 algoritmos implementados

### main.py
- ✅ Menu interativo
- ✅ Seleção de tamanho do array
- ✅ Teste individual de algoritmos
- ✅ Comparação de todos os algoritmos
- ✅ Medição de tempo precisa
- ✅ Ranking de performance
- ✅ Validação de correção

### Algoritmos (sorting/)
- ✅ Implementações corretas e testadas
- ✅ Código limpo e comentado
- ✅ API consistente (método .sort())
- ✅ Suporte para diferentes tamanhos
- ✅ Tratamento de casos especiais

## 📦 Dependências

### Python 3.7+
Requerido para funcionalidades modernas do Python

### pygame
Para visualização gráfica e sons
```bash
pip install pygame
```

### numpy
Para geração de ondas sonoras
```bash
pip install numpy
```

## 🚀 Quick Start

1. **Instalar dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Testar se funciona:**
   ```bash
   python test_sorting.py
   ```

3. **Ver visualização:**
   ```bash
   python visualizer.py
   ```

4. **Comparar algoritmos:**
   ```bash
   python main.py
   ```

## 💡 Dicas de Uso

### Para Aprender
- Use `visualizer.py` com arrays de 100-500 elementos
- Experimente diferentes algoritmos (teclas 1-7)
- Observe as cores e padrões

### Para Comparar Performance
- Use `main.py` opção 8
- Teste com 1.000, 10.000 e 100.000 elementos
- Compare os tempos de execução

### Para Desenvolver
- Veja `exemplos.py` para integrar em seu código
- Use `test_sorting.py` como referência para testes
- Adicione novos algoritmos em `sorting/`

## 📚 Recursos Adicionais

- Todos os algoritmos têm complexidade documentada
- Código-fonte comentado e legível
- Testes automatizados incluídos
- Exemplos práticos disponíveis

## ⚠️ Avisos Importantes

1. **Bogo Sort** - Apenas use com arrays de 5-8 elementos!
2. **Bubble/Insertion/Selection** - Evite arrays > 10.000 elementos
3. **Visualizador** - Arrays muito grandes (>10.000) têm frames pulados

## 🤝 Contribuindo

Para adicionar um novo algoritmo:

1. Crie arquivo em `sorting/` (ex: `counting_sort.py`)
2. Implemente classe com método `sort(array)`
3. Adicione import em `sorting/__init__.py`
4. Adicione ao menu em `main.py`
5. Adicione visualização em `visualizer.py`
6. Adicione testes em `test_sorting.py`

Exemplo:
```python
# sorting/counting_sort.py
class CountingSort:
    @staticmethod
    def sort(array):
        # Implementação
        return array
```

---

**Projeto criado para fins educacionais**
*Aprenda algoritmos de ordenação de forma visual e interativa!* 🎓
