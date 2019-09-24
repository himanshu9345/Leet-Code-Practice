"""
# Definition for a Node."""
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors



def dfs(root, new_root, seen, mapper):
    # print root.val
    for node2 in root.neighbors:
        if node2 not in seen:
            new_node2 = Node(node2.val, [])
            mapper[node2] = new_node2
            new_root.neighbors.append(new_node2)
            seen.add(node2)
            dfs(node2, new_node2, seen, mapper)
        else:
            new_root.neighbors.append(mapper[node2])
    return


class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        new_root = Node(node.val, [])
        seen = set()
        mapper = {node: new_root}

        seen.add(node)
        dfs(node, new_root, seen, mapper)
        return new_root

        """
        :type node: Node
        :rtype: Node
        """
