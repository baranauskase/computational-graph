class Node:
    """
    Represents a graph node.

    A Node in a Graph that produces an output.
    """

    def __init__(self, id):
        self.id = id
        self.output = None

class Operation(Node):
    """
    Represents a graph node that performs a compution.

    An Operation in a Graph has 0..n input nodes.
    """
    def __init__(self, id):
        super().__init__(id)
        self.input_nodes = []
        
    def compute(self, *args):
        """
        Computes the output of this operation
        """
        pass

    
class Add(Operation):
    """
    Operation for performing x+y.
    """
    def compute(self, *args):
        """
        Add numbers

        Args:
            x_value: First argument for sum
            y_value: Second argument for sum
        """

        return args[0] + args[1]

class Mul(Operation):
    """
    Operation for performing x*y
    """

    def compute(self, *args):
        """
        Multiply matrices

        Args:
            x_value: First value
            y_value: Second value
        """
        return args[0] * args[1]

class Sub(Operation):
    """
    Operation for performing x-y
    """

    def compute(self, *args):
        """
        Multiply matrices

        Args:
            x_value: First value
            y_value: Second value
        """
        return args[0] - args[1]

class Placeholder(Node):
    """
    Represents a value that is supplied at evaluation time.
    """

    def __init__(self, id, name):
        """
        Create Variable

        Args:
            initial_value: The initial value of this variable
        """
        super().__init__(id)
        self.name = name

class Variable(Node):
    """
    Represents a variable, i.e. changable parameter of a computational graph.
    """

    def __init__(self, id, initial_value=None):
        """
        Create Variable

        Args:
            initial_value: The initial value of this variable
        """
        super().__init__(id)
        self.value = initial_value

class Callback(Operation):
    """
    Represents an operation that is defined as a callback.
    """
    def __init__(self, id, callback):
        super().__init__(id)
        self._callback = callback

    def compute(self, **kwargs):
        """
        Multiply matrices

        Args:
            x_value: First value
            y_value: Second value
        """
        return self._callback(**kwargs)