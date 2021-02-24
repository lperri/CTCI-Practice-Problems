# Route between nodes: given a directed graph and two nodes (S & E), design an algorithm to find out whether there is a route from S to E
from typing import Any, List, Union
from implementation_tree_graph import GraphNode

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item: Any) -> None:
        self.queue.append(item)

    def dequeue(self) -> Any:
        return self.queue.pop(0)

    def peek(self) -> Any:
        return self.queue[0]

    def is_empty(self) -> bool:
        return len(self.queue) == 0

def is_path_between_nodes(start_node: GraphNode, target: GraphNode) -> List:
    queue = Queue()
    queue.enqueue(start_node)

    while not queue.is_empty():
        node = queue.dequeue()
        node.marked = True

        # target found! return the path
        if node.val == target.val:
            return True

        for neighbor in node.neighbors:
            if not neighbor.marked:
                queue.enqueue(neighbor)
    # no path exists
    return False


if __name__ == "__main__":
    # node_A = GraphNode(val="A")
    # node_B = GraphNode(val="B")
    # # directed graph => put in only one of the neighbor lists
    # node_A.add_neighbor(node_B)

    # node_C = GraphNode(val="C")
    # node_B.add_neighbor(node_C)

    # node_D = GraphNode(val="D")
    # node_C.add_neighbor(node_D)

    # # D points back to A
    # node_D.add_neighbor(node_A)

    node_A = GraphNode(val="A")
    node_B = GraphNode(val="B")
    node_C = GraphNode(val="C")
    node_D = GraphNode(val="D")
    node_E = GraphNode(val="E")
    node_F = GraphNode(val="F")
    node_G = GraphNode(val="G")

    node_A.add_neighbors(node_B, node_C)
    node_B.add_neighbors(node_C, node_G)
    node_C.add_neighbors(node_D)
    node_G.add_neighbors(node_E)
    node_F.add_neighbors(node_G)
    node_E.add_neighbors(node_A)

    print(is_path_between_nodes(node_A, node_E))
