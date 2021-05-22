_default_graph = None

class Placeholder:
    """
    Represents a placeholder node that has to be provided with a value when
    computing the output of the computational graph
    """

    def __init__(self):
        """
        Creates Placeholder
        """

        self.consumers = []

        _default_graph.placeholders.append(self)

class Variable:
    """
    Represents a variable, i.e. changable parameter of a computational graph.
    """

    def __init__(self, initial_value=None):
        """
        Create Variable

        Args:
            initial_value: The initial value of this variable
        """

        self.value = initial_value
        self.consumers = []

        _default_graph.variables.append(self)