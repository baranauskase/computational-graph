_default_graph = None

class Operation:
    """
    Represents a graph node that performs a compution.

    An Operation is a node in a Graph that takes zero or more objects as an
    input, and produces zero or more objects as an output.
    """

    def __init__(self, input_nodes=[]):
        """
        Creates Operation
        """

        self.input_nodes = input_nodes

        # Consumers - nodes that receive output of this operation as an input
        self.consumers = []

        # Connect this operation to inputs
        for input_node in input_nodes:
            input_node.consumers.append(self)
        
        # Update default computational graph
        _default_graph.operations.append(self)

    def compute(self):
        """
        Computes the output of this operation
        """
        pass

    
class Add(Operation):
    """
    Operation for performing x+y element-wise.
    """

    def __init__(self, x, y):
        """
        Creates Add operation.
        
        Args:
            x: First argument for sum
            y: Second argument for sum
        """

        super().__init__([x, y])

    def compute(self, x_value, y_value):
        """
        Add numbers

        Args:
            x_value: First argument for sum
            y_value: Second argument for sum
        """

        return x_value + y_value

class MatMul(Operation):
    """
    Multiplies matrix a by matrix b, producing a * b
    """

    def __init__(self, a, b):
        """
        Creates MatMul

        Args:
            a: First matrix
            b: Second matrix
        """
        super().__init__([a, b])

    def compute(self, a_value, b_value):
        """
        Multiply matrices

        Args:
            a_value: First matrix value
            b_value: Second matrix value
        """
        return a_value.dot(b_value)
