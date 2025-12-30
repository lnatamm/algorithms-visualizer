class SelectionSort:
    
    @staticmethod
    def sort(array):
        """Selection Sort - Encontra o menor elemento e o coloca na posição correta"""
        n = len(array)
        
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if array[j] < array[min_idx]:
                    min_idx = j
            
            array[i], array[min_idx] = array[min_idx], array[i]
        
        return array
