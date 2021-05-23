import pytest
from comp_graph.extensions import sphere_volume, cylinder_volume

@pytest.mark.parametrize('r, expected', [
    (
        1,
        4.19
    ),
    (
        2,
        33.51
    ),
])
def test_sphere_volume(r, expected):
    v = sphere_volume(r)
    assert abs(v-expected) < 1e-2

@pytest.mark.parametrize('r, h, expected', [
    (
        1,
        1,
        3.14
    ),
    (
        2,
        2,
        25.13
    ),
])
def test_cylinder_volume(r, h, expected):
    v = cylinder_volume(r, h)
    assert abs(v-expected) < 1e-2