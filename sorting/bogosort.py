import random

class BogoSort:
    
    @staticmethod
    def is_sorted(array):
        """Verifica se o array está ordenado"""
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                return False
        return True
    
    @staticmethod
    def sort(array, max_iterations=1000000):
        """Bogo Sort - Embaralha aleatoriamente até ficar ordenado (MUITO INEFICIENTE!)"""
        iterations = 0
        while not BogoSort.is_sorted(array) and iterations < max_iterations:
            random.shuffle(array)
            iterations += 1
        
        if iterations >= max_iterations:
            print(f"BogoSort atingiu o limite de {max_iterations} iterações!")
        
        return array
