from __future__ import annotations
from typing import Generic, TypeVar

T = TypeVar("T")
I = TypeVar("I")

class Percentiles(Generic[T]):

    def __init__(self) -> None:
        pass

    def ratio(self, x: float, y: float):
        raise NotImplementedError()

    def add_point(item: T) -> None:
        raise NotImplementedError()

    def remove_point(item: T) -> None:
        raise NotImplementedError()
        
if __name__ == "__main__":
    points = list(enumerate(list(range(50))))
    import random
    random.shuffle(points)
    p = Percentiles(points)
    # Numbers from 8 to 16.
    print(p.ratio(15, 66))
