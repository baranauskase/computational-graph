from comp_graph import Placeholder, Variable
from comp_graph.operations import Operation
import numpy as np

class Session:
    """
    Represents a particular execution of a computational graph
    """

    def run(self, operation, feed_dict={}):

        # Perform a post order traversal of the graph to bring the nodes into
        # the right order order
        nodes_postorder = self.traverse_postorder(operation)

        for node in nodes_postorder:
            # Calculate node values:
            if type(node) == Placeholder:
                # Placeholder inputed constants
                node.output = feed_dict[node]
            elif type(node) == Variable:
                # Variable value becomes its output
                node.output = node.value
            else:
                # We are dealing with operation
                node.inputs = [input_node.output for input_node in node.input_nodes]
                node.output = node.compute(*node.inputs)

            # Convert lists to numpy arrays to get free matrix/vector arithmetic
            if type(node.output) == list:
                node.output = np.array(node.output)

            
        return operation.output


    def traverse_postorder(self, operation):
        """
        Performs a post order traversal, returning a list of nodes in the order
        in which they have to be computed

        Args:
            operation: The operation to start traversal at
        """
        nodes_postorder = []
        def traverse(node):
            if isinstance(node, Operation):
                for input_node in node.input_nodes:
                    traverse(input_node)
            nodes_postorder.append(node)

        traverse(operation)
        return nodes_postorder
