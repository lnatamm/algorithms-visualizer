class BubbleSort:
    
    @staticmethod
    def sort(array):
        """Bubble Sort - Compara elementos adjacentes e os troca se estiverem na ordem errada"""
        n = len(array)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    swapped = True
            
            # Se nenhuma troca foi feita, o array já está ordenado
            if not swapped:
                break
        
        return array
