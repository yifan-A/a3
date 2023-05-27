from __future__ import annotations
from typing import Generic, TypeVar
from math import ceil
from bst import BinarySearchTree

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        self.bst = BinarySearchTree()
    
    def add_point(self, item: T):
        self.bst[item] = 1
    
    def remove_point(self, item: T):
        del self.bst[item]

    def ratio(self, x, y):
        size = len(self.bst)
        result = []
        x = x * 0.01
        y = y * 0.01
        
        for i in range(size):
            if i / size >= x and (size - 1 - i) / size >= y:
                result.append(self.bst.kth_smallest(i+1, self.bst.root).key)
        return result

if __name__ == "__main__":
    points = list(range(50))
    import random
    random.shuffle(points)
    p = Percentiles()
    for point in points:
        p.add_point(point)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))