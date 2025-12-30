class MergeSort:
    
    @staticmethod
    def merge(array, left, mid, right):
        """Mescla dois subarrays ordenados"""
        left_array = array[left:mid+1]
        right_array = array[mid+1:right+1]
        
        i = j = 0
        k = left
        
        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                array[k] = left_array[i]
                i += 1
            else:
                array[k] = right_array[j]
                j += 1
            k += 1
        
        while i < len(left_array):
            array[k] = left_array[i]
            i += 1
            k += 1
        
        while j < len(right_array):
            array[k] = right_array[j]
            j += 1
            k += 1
    
    @staticmethod
    def sort(array, left=0, right=None):
        """Merge Sort - Divisão e conquista"""
        if right is None:
            right = len(array) - 1
        
        if left < right:
            mid = (left + right) // 2
            MergeSort.sort(array, left, mid)
            MergeSort.sort(array, mid + 1, right)
            MergeSort.merge(array, left, mid, right)
        
        return array
