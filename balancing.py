from __future__ import annotations
from threedeebeetree import Point, ThreeDeeBeeTree, BeeNode

def make_ordering(my_coordinate_list: list[Point]) -> list[Point]:
    raise NotImplementedError()

if __name__ == "__main__":
    import random
    points = []
    coords = list(range(10000))
    random.shuffle(coords)
    for i in range(3000):
        point = (coords[3*i], coords[3*i+1], coords[3*i+2])
        points.append(point)

    ordering = make_ordering(points)
    tdbt = ThreeDeeBeeTree()
    for p in ordering:
        tdbt[p] = "A"
    def get_size(node):
        if node is None:
            return 0
        return node.subtree_size

    # Testing function to calculate the worst ratio on your 3️⃣🇩🐝🌳
    def collect_worst_ratio(node: BeeNode):
        default = (1, 0, "")
        if node is None:
            return default
        root_level = node.key
        neg_x_pos_y_pos_z = node.get_child_for_key((root_level[0]-1, root_level[1]+1, root_level[2]+1))
        neg_x_pos_y_neg_z = node.get_child_for_key((root_level[0]-1, root_level[1]+1, root_level[2]-1))
        neg_x_neg_y_pos_z = node.get_child_for_key((root_level[0]-1, root_level[1]-1, root_level[2]+1))
        neg_x_neg_y_neg_z = node.get_child_for_key((root_level[0]-1, root_level[1]-1, root_level[2]-1))
        pos_x_pos_y_pos_z = node.get_child_for_key((root_level[0]+1, root_level[1]+1, root_level[2]+1))
        pos_x_pos_y_neg_z = node.get_child_for_key((root_level[0]+1, root_level[1]+1, root_level[2]-1))
        pos_x_neg_y_pos_z = node.get_child_for_key((root_level[0]+1, root_level[1]-1, root_level[2]+1))
        pos_x_neg_y_neg_z = node.get_child_for_key((root_level[0]+1, root_level[1]-1, root_level[2]-1))
        pos_x = sum(get_size(n) for n in [
            pos_x_neg_y_neg_z,
            pos_x_neg_y_pos_z,
            pos_x_pos_y_neg_z,
            pos_x_pos_y_pos_z,
        ])
        neg_x = sum(get_size(n) for n in [
            neg_x_neg_y_neg_z,
            neg_x_neg_y_pos_z,
            neg_x_pos_y_neg_z,
            neg_x_pos_y_pos_z,
        ])
        pos_y = sum(get_size(n) for n in [
            neg_x_pos_y_neg_z,
            neg_x_pos_y_pos_z,
            pos_x_pos_y_neg_z,
            pos_x_pos_y_pos_z,
        ])
        neg_y = sum(get_size(n) for n in [
            neg_x_neg_y_neg_z,
            neg_x_neg_y_pos_z,
            pos_x_neg_y_neg_z,
            pos_x_neg_y_pos_z,
        ])
        pos_z = sum(get_size(n) for n in [
            neg_x_neg_y_pos_z,
            neg_x_pos_y_pos_z,
            pos_x_neg_y_pos_z,
            pos_x_pos_y_pos_z,
        ])
        neg_z = sum(get_size(n) for n in [
            neg_x_neg_y_neg_z,
            neg_x_pos_y_neg_z,
            pos_x_neg_y_neg_z,
            pos_x_pos_y_neg_z,
        ])
        if pos_x >= 12 or neg_x >= 12:
            try:
                default = max(default, (pos_x/neg_x, neg_x, "x"), (neg_x/pos_x, pos_x, "x"))
            except ZeroDivisionError:
                default = (float('inf'), (pos_x, neg_x), "x")
        if pos_y >= 12 or neg_y >= 12:
            try:
                default = max(default, (pos_y/neg_y, neg_y, "y"), (neg_y/pos_y, pos_y, "y"))
            except ZeroDivisionError:
                default = (float('inf'), (pos_y, neg_y), "y")
        if pos_z >= 12 or neg_z >= 12:
            try:
                default = max(default, (pos_z/neg_z, neg_z, "z"), (neg_z/pos_z, pos_z, "z"))
            except ZeroDivisionError:
                default = (float('inf'), (pos_z, neg_z), "z")
        return max(default, default, *(collect_worst_ratio(child) for child in [
            neg_x_neg_y_neg_z,
            neg_x_neg_y_pos_z,
            neg_x_pos_y_neg_z,
            neg_x_pos_y_pos_z,
            pos_x_neg_y_neg_z,
            pos_x_neg_y_pos_z,
            pos_x_pos_y_neg_z,
            pos_x_pos_y_pos_z,
        ]))

    ratio, smaller, axis = collect_worst_ratio(tdbt.root)
    print(f"Worst ratio is 1:{ratio:.2f}, with sizes {smaller}:{int(smaller*ratio)} which occurs on the {axis} axis.")

