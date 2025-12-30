"""
Módulo de algoritmos de ordenação
"""

from .quicksort import QuickSort
from .mergesort import MergeSort
from .heapsort import HeapSort
from .bubblesort import BubbleSort
from .insertionsort import InsertionSort
from .selectionsort import SelectionSort
from .bogosort import BogoSort

__all__ = [
    'QuickSort',
    'MergeSort',
    'HeapSort',
    'BubbleSort',
    'InsertionSort',
    'SelectionSort',
    'BogoSort',
]
