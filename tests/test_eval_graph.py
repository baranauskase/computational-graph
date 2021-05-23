import pytest
from comp_graph import eval_graph


@pytest.mark.parametrize('path, placeholder_vals, expected', [
    (
        'example_graphs/sum',
        {},
        3
    ),
    (
        'example_graphs/product-of-sums',
        {},
        21
    ),
    (
        'example_graphs/multi-edge',
        {},
        2
    ),
    (
        'example_graphs/diff-of-products',
        {'x': 4, 'y': 5},
        -7
    ),
    (
        'example_graphs/coloured-graph-expanded',
        {'r': 2, 'h': 3},
        71.20943348136865
    ),
    (
        'example_graphs/coloured-graph',
        {'r': 2, 'h': 3},
        71.20943348136865
    ),
    (
        'example_graphs/function-call-expanded',
        {'r': 2, 'h': 3},
        71.20943348136865
    ),
    (
        'example_graphs/function-call',
        {'r': 2, 'h': 3},
        71.20943348136865
    )
])
def test_eval_graph(path, placeholder_vals, expected):
    res = eval_graph(path, placeholder_vals)
    assert res == expected
