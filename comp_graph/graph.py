import comp_graph.operations as operations
import comp_graph.values as values

class Graph:
    """
    Represents a computational graph
    """

    def __init__(self):
        """
        Create graph
        """

        self.operations = []
        self.placeholders = []
        self.variables = []

    def as_default(self):
        operations._default_graph = self
        values._default_graph = self
