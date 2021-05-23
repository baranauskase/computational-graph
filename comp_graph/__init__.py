import csv
import math
from comp_graph.graph import Graph
from comp_graph.session import Session
from comp_graph.nodes import Add, Mul, Sub, Variable, Placeholder, Callback
from comp_graph.extensions import sphere_volume, cylinder_volume, pi

def _read_csv(path):
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)

def _make_extension(name):
    if name == 'sphere volume':
        return sphere_volume
    elif name == 'cylinder volume':
        return cylinder_volume
    elif name == 'pi':
        return pi
    return None

def _make_node(id, name, color=None):
    simple_variable = None
    try:
        simple_variable = Variable(id, int(name))
    except ValueError:
        try:
            simple_variable = Variable(id, float(name))
        except ValueError:
            pass
    
    callback = _make_extension(name)

    if name == '+':
        return Add(id)
    elif name  == '*':
        return Mul(id)
    elif name == '-':
        return Sub(id)
    elif callback:
        return Callback(id, callback)
    elif '/' in name:
        # Fraction
        nums = [int(n) for n in name.split('/')]
        value = nums[0] / nums[1]
        return Variable(id, value)
    elif simple_variable:
        return simple_variable
    else:
        return Placeholder(id, name)


def _make_graph(nodes, edges):
    g = Graph()
    
    for n in nodes:
        g.add_vertex(_make_node(**n))
    
    for edge in edges:
        g.add_edge(**edge)  

    return g

def eval_graph(path, placeholder_vals):
    """
    Evaluates graph
    """
    edges_path = f'{path}.edges.csv'
    nodes_path = f'{path}.nodes.csv'
    edges = _read_csv(edges_path)
    nodes = _read_csv(nodes_path)
    g = _make_graph(nodes, edges)

    output = Session().run(g, placeholder_vals)
    return output