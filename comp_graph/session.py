from comp_graph.nodes import Variable, Placeholder, Operation, Callback

class Session:
    """
    Represents a particular execution of a computational graph
    """

    def run(self, graph, placeholder_vals):
        leaf_nodes = graph.leaf_nodes()
        if len(leaf_nodes) != 1:
            raise IOError('Invalid computational graph encountered')

        operation = leaf_nodes[0]

        # Perform a post order traversal of the graph to bring the nodes into
        # the right order order
        nodes_postorder = self.traverse_postorder(operation)

        for node in nodes_postorder:
            # Calculate node values:
            if type(node) == Placeholder:
                # Placeholder inputed constants
                if node.name in placeholder_vals:
                    node.output = placeholder_vals[node.name]
                else:
                    raise IOError(f'Missing value for {node.name}')
            elif type(node) == Variable:
                # Variable value becomes its output
                node.output = node.value
            elif type(node) == Callback:
                inputs = [input_node for input_node in node.input_nodes]
                named_inputs = {i.name: i.output for i in inputs}
                node.output = node.compute(**named_inputs)
            else:
                # We are dealing with simple operation
                node.inputs = [input_node.output for input_node in node.input_nodes]
                node.output = node.compute(*node.inputs)
            
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
