"""
Exemplos de uso dos algoritmos de ordenação
"""

from sorting import QuickSort, MergeSort, HeapSort, BubbleSort, InsertionSort, SelectionSort
import random
import time

def exemplo_basico():
    """Exemplo básico de uso"""
    print("=" * 60)
    print("EXEMPLO BÁSICO - Ordenando um array pequeno")
    print("=" * 60)
    
    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nArray original: {array}")
    
    # Testando QuickSort
    array_copy = array.copy()
    sorted_array = QuickSort.sort(array_copy)
    print(f"QuickSort:      {sorted_array}")
    
    # Testando MergeSort
    array_copy = array.copy()
    sorted_array = MergeSort.sort(array_copy)
    print(f"MergeSort:      {sorted_array}")
    
    # Testando HeapSort
    array_copy = array.copy()
    sorted_array = HeapSort.sort(array_copy)
    print(f"HeapSort:       {sorted_array}")

def exemplo_performance():
    """Exemplo de comparação de performance"""
    print("\n" + "=" * 60)
    print("EXEMPLO DE PERFORMANCE - Arrays maiores")
    print("=" * 60)
    
    sizes = [100, 1000, 5000]
    algorithms = [
        ("QuickSort", QuickSort.sort),
        ("MergeSort", MergeSort.sort),
        ("HeapSort", HeapSort.sort),
        ("BubbleSort", BubbleSort.sort),
        ("InsertionSort", InsertionSort.sort),
        ("SelectionSort", SelectionSort.sort),
    ]
    
    for size in sizes:
        print(f"\n--- Array de {size} elementos ---")
        array = random.sample(range(1, size * 10), size)
        
        for name, func in algorithms:
            # Pula algoritmos lentos para arrays grandes
            if size > 1000 and name in ["BubbleSort", "InsertionSort", "SelectionSort"]:
                print(f"{name:15} - Pulado (muito lento para {size} elementos)")
                continue
            
            array_copy = array.copy()
            start = time.time()
            func(array_copy)
            elapsed = time.time() - start
            print(f"{name:15} - {elapsed:.6f} segundos")

def exemplo_ordenacao_customizada():
    """Exemplo de uso com diferentes tipos de dados"""
    print("\n" + "=" * 60)
    print("EXEMPLO - Diferentes tipos de dados")
    print("=" * 60)
    
    # Array de números
    numeros = [5, 2, 8, 1, 9]
    print(f"\nNúmeros antes:  {numeros}")
    QuickSort.sort(numeros)
    print(f"Números depois: {numeros}")
    
    # Array já ordenado
    ordenado = [1, 2, 3, 4, 5]
    print(f"\nJá ordenado antes:  {ordenado}")
    start = time.time()
    QuickSort.sort(ordenado)
    elapsed = time.time() - start
    print(f"Já ordenado depois: {ordenado} ({elapsed:.8f}s)")
    
    # Array invertido (pior caso para alguns algoritmos)
    invertido = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"\nInvertido antes:  {invertido}")
    start = time.time()
    MergeSort.sort(invertido)
    elapsed = time.time() - start
    print(f"Invertido depois: {invertido} ({elapsed:.8f}s)")

if __name__ == "__main__":
    exemplo_basico()
    exemplo_performance()
    exemplo_ordenacao_customizada()
    
    print("\n" + "=" * 60)
    print("Para visualização gráfica, execute: python visualizer.py")
    print("Para menu interativo, execute: python main.py")
    print("=" * 60)
