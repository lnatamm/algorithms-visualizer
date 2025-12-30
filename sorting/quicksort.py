class QuickSort:

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                aux = array[i]
                array[i] = array[j]
                array[j] = aux
        aux = array[i + 1]
        array[i + 1] = array[high]
        array[high] = aux
        return i + 1

    @staticmethod
    def sort(array: list, low: int=0, high: int=None):
        if high is None:
            high = len(array) - 1
        if low < high:
            pi = QuickSort.partition(array, low, high)
            QuickSort.sort(array, low, pi - 1)
            QuickSort.sort(array, pi + 1, high)
        return array