class HeapSort:
    
    @staticmethod
    def heapify(array, n, i):
        """Transforma o array em um heap máximo"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and array[left] > array[largest]:
            largest = left
        
        if right < n and array[right] > array[largest]:
            largest = right
        
        if largest != i:
            array[i], array[largest] = array[largest], array[i]
            HeapSort.heapify(array, n, largest)
    
    @staticmethod
    def sort(array):
        """Heap Sort - Ordenação usando estrutura de heap"""
        n = len(array)
        
        # Constrói o heap máximo
        for i in range(n // 2 - 1, -1, -1):
            HeapSort.heapify(array, n, i)
        
        # Extrai elementos do heap um por um
        for i in range(n - 1, 0, -1):
            array[0], array[i] = array[i], array[0]
            HeapSort.heapify(array, i, 0)
        
        return array
