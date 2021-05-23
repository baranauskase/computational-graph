class Graph:
    """
    Represents a computational graph
    """

    def __init__(self):
        """
        Create a graph
        """
        self._vertices = {}
        self._edges = {}

    def add_vertex(self, vertex):
        if vertex.id not in self._vertices:
            self._vertices[vertex.id] = vertex

    def add_edge(self, source, dest):
        source_node = self._vertices[source]
        dest_node = self._vertices[dest]
        dest_node.input_nodes.append(source_node)

        if source in self._edges:
            self._edges[source].append(dest_node)
        else:
            self._edges[source] = [dest_node]

    def leaf_nodes(self):
        leaves = []
        for id, node in self._vertices.items():
            if id not in self._edges:
                leaves.append(node)
        return leaves
            

