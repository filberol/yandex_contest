nodes = int(input())
langs = input().split(' ')
digits = list(map(lambda x: int(x), input().split(' ')))


class Node:
    def __init__(self, idf, language):
        self.idf = idf
        self.language = language
        self.parent: Node | None = None

    def count_barrier(self, await_lang):
        curr_barrier = 0
        curr_n = self
        while curr_n.parent.idf != 0 and curr_n.parent.language != await_lang:
            curr_barrier += 1
            curr_n = curr_n.parent
        return curr_barrier

    def find_parent(self, value):
        curr_n = self
        while curr_n.idf != value:
            curr_n = curr_n.parent
        return curr_n


res = [0] * nodes
curr_node = Node(0, None)
opened_nodes = set()
for dig_ind, digit in enumerate(digits):
    if digit == 0:
        continue
    if digit not in opened_nodes:
        # print(f"add node {digit} to node {curr_node.idf}")
        opened_nodes.add(digit)
        dummy = Node(digit, langs[digit - 1])
        dummy.parent = curr_node
        curr_node = dummy
    else:
        ret_node = curr_node.find_parent(digit)
        # print(f"on node {digit} backed to node {ret_node.idf} with parent {ret_node.parent.idf}")
        curr_node = ret_node
        depth = curr_node.count_barrier(curr_node.language)
        # print(f"counted barrier as {depth}")
        res[digit - 1] = depth
        curr_node = curr_node.parent

print(*res, sep=' ')
