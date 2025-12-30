class InsertionSort:
    
    @staticmethod
    def sort(array):
        """Insertion Sort - Constrói a lista ordenada um elemento por vez"""
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            
            while j >= 0 and array[j] > key:
                array[j + 1] = array[j]
                j -= 1
            
            array[j + 1] = key
        
        return array
