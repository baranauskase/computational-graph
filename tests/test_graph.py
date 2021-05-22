from comp_graph import (
    Graph,
    Variable,
    Placeholder,
    MatMul,
    Add,
    Session
)

def test_graph():
    """
    z = [[1, 0], [0, -1]] * x + [1, 1],
    where x is [1, 2]
    """
    x_val = [1, 2]
    z_expected = [2, -1]

    Graph().as_default()

    # Variables
    A = Variable([[1, 0], [0, -1]])
    b = Variable([1, 1])

    # Placeholder
    x = Placeholder()

    # Hidden node y
    y = MatMul(A, x)

    # Output node z
    z = Add(y, b)


    session = Session()
    output = session.run(z, {
        x: x_val
    })

    assert output.tolist() == z_expected


