from __future__ import annotations
from typing import List
from beehive import Beehive

class BeehiveSelector:

    def __init__(self) -> None:
        pass

    def set_all_beehives(hive_list: List[Beehive]):
        raise NotImplementedError()

    def add_beehive(self, hive: Beehive):
        raise NotImplementedError()

    def harvest_best_beehive(self) -> float:
        """
        Harvest the maximum amount of honey from the most profitable beehive.
        If the volume of this beehive is now 0, remove it from the selector.
        """
        raise NotImplementedError()
