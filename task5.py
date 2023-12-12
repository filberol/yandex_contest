import math


class Node:
    def __init__(self):
        self.nodes_in_place = 1
        self.child_nodes: dict[int, Node] = {}


root_nodes = {}
every_node = set()

array_count = int(input())
arrays = []
arrays_length = []
for i in range(array_count):
    arrays_length.append(int(input()))
    new_arr = list(map(lambda x: int(x), input().split(' ')))
    f_val = new_arr[0]
    if f_val not in root_nodes:
        new_node = Node()
        root_nodes[f_val] = new_node
        every_node.add(new_node)
    else:
        root_nodes[f_val].nodes_in_place += 1
    arrays.append(new_arr)

for a_ind, array in enumerate(arrays):
    curr_node = root_nodes[array[0]]
    for curr_depth in range(1, arrays_length[a_ind]):
        val = array[curr_depth]
        if val not in curr_node.child_nodes:
            new_node = Node()
            curr_node.child_nodes[val] = new_node
            every_node.add(new_node)
            curr_node = new_node
        else:
            curr_node = curr_node.child_nodes[val]
            curr_node.nodes_in_place += 1

count = 0
for node in every_node:
    count += math.comb(node.nodes_in_place, 2)

print(count)



