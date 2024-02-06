import pytest
from gcl_alg import gcl_alg


def test_gcl_alg():
    assert gcl_alg(0,0,0,1)>109 and gcl_alg(0,0,0,1)<113 #this tests to see if the distance between one degree longitud is correct
    assert gcl_alg(0,78,0,79)>109 and gcl_alg(0,78,0,79)<113

def test_gcl_alg_exceptions():
    with pytest.raises(TypeError):
        gcl_alg('asdf', 0, 0,0)
