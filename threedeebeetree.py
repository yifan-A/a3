from __future__ import annotations
from typing import Generic, TypeVar, Tuple, List
from dataclasses import dataclass, field

I = TypeVar('I')
Point = Tuple[int, int, int]

@dataclass
class BeeNode:

    key: Point
    item: I
    subtree_size: int = 1
    subtree:List[BeeNode|None] = field(default_factory=list)

    # time complexity O(1)
    def get_index_for_key(self, point: Point)->int:
        if len(self.subtree) == 0:
            for i in range(8):
                self.subtree.append(None)
        idx = 0
        if point[0] > self.key[0]:
            idx |= 1
        if point[1] > self.key[1]:
            idx |= 2
        if point[2] > self.key[2]:
            idx |= 4
        return idx
    # time complexity O(1)
    def get_child_for_key(self, point: Point) -> BeeNode:
        # raise NotImplementedError()
        idx = self.get_index_for_key(point)
        return self.subtree[idx]
    # time complexity O(1)
    def set_node_for_key(self,point:Point,node:BeeNode)->None:
        idx = self.get_index_for_key(point)
        self.subtree[idx] = node



class ThreeDeeBeeTree(Generic[I]):
    """ 3️⃣🇩🐝🌳 tree. """

    def __init__(self) -> None:
        """
            Initialises an empty 3DBT
        """
        self.root = None
        self.length = 0

    def is_empty(self) -> bool:
        """
            Checks to see if the 3DBT is empty
        """
        return len(self) == 0

    def __len__(self) -> int:
        """ Returns the number of nodes in the tree. """

        return self.length

    def __contains__(self, key: Point) -> bool:
        """
            Checks to see if the key is in the 3DBT
        """
        try:
            self.get_tree_node_by_key(key)
            return True
        except KeyError:
            return False

    def __getitem__(self, key: Point) -> I:
        """
            Attempts to get an item in the tree, it uses the Key to attempt to find it
        """
        node = self.get_tree_node_by_key(key)
        return node.item

    # time complexity O(D)
    # D is the depth of tree
    def get_tree_node_by_key(self, key: Point) -> BeeNode:
        # raise NotImplementedError()
        current = self.root
        while current is not None:
            eq = True
            for i in range(3):
                if key[i] != current.key[i]:
                    eq = False
                    break
            if eq == True:
                break
            current = current.get_child_for_key(key)
        return current

    def __setitem__(self, key: Point, item: I) -> None:
        self.root = self.insert_aux(self.root, key, item)

    # time complexity O(D)
    # D is the depth of tree
    def insert_aux(self, current: BeeNode, key: Point, item: I) -> BeeNode:
        """
            Attempts to insert an item into the tree, it uses the Key to insert it
        """
        # raise NotImplementedError()
        if current is None:
            current = BeeNode(key,item,1)
            return current
        child = current.get_child_for_key(key)
        child = self.insert_aux(child,key,item)
        current.set_node_for_key(key,child)
        current.subtree_size = 1
        for i in range(8):
            if current.subtree[i] is not None:
                current.subtree_size += current.subtree[i].subtree_size
        return current

    def is_leaf(self, current: BeeNode) -> bool:
        """ Simple check whether or not the node is a leaf. """
        # raise NotImplementedError()
        for i in range(8):
            if current.subtree[i] is not None:
                return False
        return True

if __name__ == "__main__":
    tdbt = ThreeDeeBeeTree()
    tdbt[(3, 3, 3)] = "A"
    tdbt[(1, 5, 2)] = "B"
    tdbt[(4, 3, 1)] = "C"
    tdbt[(5, 4, 0)] = "D"
    print(tdbt.root.get_child_for_key((4, 3, 1)).subtree_size) # 2