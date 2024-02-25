from iss_tracker import range_summary, print_full_epoch, calc_avg_speed
import pytest

def test_calc_avg_speed():
    assert calc_avg_speed([{'a': {'#text':1}}], ['a']) == 1.0
    assert calc_avg_speed([{'a': {'#text':1}},{'a': {'#text':2}}], ['a']) == 1.5
def test_calc_avg_speed_exceptions():
    with pytest.raises(ValueError):
        calc_avg_speed([{'a': {'#text':'c'}}], ['a'])         # character input instead of float
    with pytest.raises(TypeError):
        calc_avg_speed([['a','b', 'c'], ['a']])


def test_print_full_epoch():
    assert print_full_epoch([{'a': {'#text':1}}], 0) == None
def test_range_summary():
    assert range_summary([{'a': {'#text':1}}], 0) == None

