"""
Testes simples para verificar a correção dos algoritmos
"""

from sorting import (QuickSort, MergeSort, HeapSort, 
                     BubbleSort, InsertionSort, SelectionSort, BogoSort)
import random

def test_algorithm(name, sort_func, test_arrays):
    """Testa um algoritmo com diferentes casos"""
    print(f"\n{'='*50}")
    print(f"Testando: {name}")
    print('='*50)
    
    all_passed = True
    
    for i, test_case in enumerate(test_arrays, 1):
        original = test_case['array'].copy()
        expected = test_case['expected']
        description = test_case['description']
        
        # Executa o algoritmo
        if name == "BogoSort" and len(original) > 8:
            print(f"  {i}. {description}: PULADO (array muito grande)")
            continue
            
        result = sort_func(original)
        
        # Verifica se está correto
        passed = result == expected
        status = "✓ PASS" if passed else "✗ FAIL"
        
        if passed:
            print(f"  {i}. {description}: {status}")
        else:
            print(f"  {i}. {description}: {status}")
            print(f"     Esperado: {expected}")
            print(f"     Obtido:   {result}")
            all_passed = False
    
    return all_passed

def main():
    print("\n" + "="*60)
    print("  TESTES DE CORREÇÃO DOS ALGORITMOS")
    print("="*60)
    
    # Casos de teste
    test_arrays = [
        {
            'array': [5, 2, 8, 1, 9],
            'expected': [1, 2, 5, 8, 9],
            'description': 'Array simples'
        },
        {
            'array': [1, 2, 3, 4, 5],
            'expected': [1, 2, 3, 4, 5],
            'description': 'Já ordenado'
        },
        {
            'array': [5, 4, 3, 2, 1],
            'expected': [1, 2, 3, 4, 5],
            'description': 'Ordem inversa'
        },
        {
            'array': [3],
            'expected': [3],
            'description': 'Um elemento'
        },
        {
            'array': [],
            'expected': [],
            'description': 'Array vazio'
        },
        {
            'array': [5, 5, 5, 5],
            'expected': [5, 5, 5, 5],
            'description': 'Elementos iguais'
        },
        {
            'array': [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],
            'expected': [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9],
            'description': 'Com duplicatas'
        },
        {
            'array': list(range(20, 0, -1)),
            'expected': list(range(1, 21)),
            'description': '20 elementos invertidos'
        },
    ]
    
    # Lista de algoritmos
    algorithms = [
        ('QuickSort', QuickSort.sort),
        ('Merge Sort', MergeSort.sort),
        ('Heap Sort', HeapSort.sort),
        ('Bubble Sort', BubbleSort.sort),
        ('Insertion Sort', InsertionSort.sort),
        ('Selection Sort', SelectionSort.sort),
        ('BogoSort', BogoSort.sort),
    ]
    
    # Testa cada algoritmo
    results = {}
    for name, func in algorithms:
        passed = test_algorithm(name, func, test_arrays)
        results[name] = passed
    
    # Resumo final
    print("\n" + "="*60)
    print("  RESUMO DOS TESTES")
    print("="*60)
    
    all_passed = True
    for name, passed in results.items():
        status = "✓ TODOS OS TESTES PASSARAM" if passed else "✗ ALGUNS TESTES FALHARAM"
        print(f"{name:20} {status}")
        if not passed:
            all_passed = False
    
    print("="*60)
    
    if all_passed:
        print("\n🎉 SUCESSO! Todos os algoritmos estão funcionando corretamente!")
    else:
        print("\n⚠️  ATENÇÃO! Alguns algoritmos falharam nos testes.")
    
    print("\nPara visualização gráfica, execute: python visualizer.py")
    print("Para testes de performance, execute: python main.py")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
