class Node:
    def __init__(self, d):
        self.data = d
        self.neighbors = []


def clone_rec(root, nodes_completed):
    if root == None:
        return None
    pNew = Node(root.data)
    nodes_completed[root] = pNew

    for p in root.neighbors:
        x = nodes_completed.get(p)
        if x == None:
            pNew.neighbors += [clone_rec(p, nodes_completed)]
        else:
            pnew.neighbors += [x]
    return pNew


def clone(root):
    nodes_completed = {}
    return clone_rec(root, nodes_completed)  # return root


"""
We use depth-first traversal and create a copy of each node while traversing the graph. To avoid getting stuck in cycles, we’ll use a hashtable to store each completed node and will not revisit nodes that exist in the hashtable. The hashtable key will be a node in the original graph, and its value will be the corresponding node in the cloned graph.


"""