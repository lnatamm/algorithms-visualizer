from sorting.quicksort import QuickSort
from sorting.mergesort import MergeSort
from sorting.heapsort import HeapSort
from sorting.bubblesort import BubbleSort
from sorting.insertionsort import InsertionSort
from sorting.selectionsort import SelectionSort
from sorting.bogosort import BogoSort
import random
import time

def print_menu():
    print("\n" + "="*60)
    print("  MENU DE ALGORITMOS DE ORDENAÇÃO")
    print("="*60)
    print("1. QuickSort")
    print("2. Merge Sort")
    print("3. Heap Sort")
    print("4. Bubble Sort")
    print("5. Insertion Sort")
    print("6. Selection Sort")
    print("7. Bogo Sort (CUIDADO - Muito lento!)")
    print("8. Testar TODOS os algoritmos")
    print("0. Sair")
    print("="*60)

def test_algorithm(algo_name, sort_func, array_copy, *args):
    print(f"\nTestando {algo_name}...")
    test_array = array_copy.copy()
    start_time = time.time()
    
    if args:
        sorted_array = sort_func(test_array, *args)
    else:
        sorted_array = sort_func(test_array)
    
    end_time = time.time()
    elapsed = end_time - start_time
    
    # Verifica se está ordenado
    is_sorted = all(sorted_array[i] <= sorted_array[i+1] for i in range(len(sorted_array)-1))
    status = "✓ SUCESSO" if is_sorted else "✗ FALHOU"
    
    print(f"{status} - {algo_name} completou em {elapsed:.6f} segundos")
    return elapsed

def main():
    while True:
        print_menu()
        choice = input("\nEscolha uma opção: ").strip()
        
        if choice == '0':
            print("Saindo...")
            break
        
        if choice not in ['1', '2', '3', '4', '5', '6', '7', '8']:
            print("Opção inválida! Tente novamente.")
            continue
        
        # Solicita tamanho do array
        try:
            size = int(input("Digite o tamanho do array (ex: 1000, 10000, 100000): ").strip())
            if size <= 0:
                print("Tamanho deve ser positivo!")
                continue
            
            # Aviso para Bogo Sort
            if choice == '7' and size > 10:
                confirm = input(f"AVISO: Bogo Sort com {size} elementos pode demorar MUITO! Continuar? (s/n): ")
                if confirm.lower() != 's':
                    continue
            
        except ValueError:
            print("Valor inválido!")
            continue
        
        # Gera array aleatório
        print(f"\nGerando array de {size} elementos...")
        array = random.sample(range(1, size * 10), size)
        
        algorithms = {
            '1': ('QuickSort', QuickSort.sort),
            '2': ('Merge Sort', MergeSort.sort),
            '3': ('Heap Sort', HeapSort.sort),
            '4': ('Bubble Sort', BubbleSort.sort),
            '5': ('Insertion Sort', InsertionSort.sort),
            '6': ('Selection Sort', SelectionSort.sort),
            '7': ('Bogo Sort', BogoSort.sort),
        }
        
        if choice == '8':
            print("\n" + "="*60)
            print("  TESTE COMPARATIVO - TODOS OS ALGORITMOS")
            print("="*60)
            results = []
            
            # Testa todos exceto Bogo Sort se array for grande
            for key, (name, func) in algorithms.items():
                if key == '7' and size > 10:
                    print(f"\n⊗ Pulando {name} (array muito grande)")
                    continue
                
                elapsed = test_algorithm(name, func, array)
                results.append((name, elapsed))
            
            # Mostra ranking
            print("\n" + "="*60)
            print("  RANKING DE DESEMPENHO")
            print("="*60)
            results.sort(key=lambda x: x[1])
            for i, (name, elapsed) in enumerate(results, 1):
                print(f"{i}. {name}: {elapsed:.6f} segundos")
        else:
            name, func = algorithms[choice]
            test_algorithm(name, func, array)
        
        input("\nPressione ENTER para continuar...")

if __name__ == "__main__":
    main()