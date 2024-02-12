from ml_data_reader import max_mass, min_mass
import pytest

def test_max_mass():
    assert max_mass([{'a': 1}], 'a')[1] == 1.0
    assert max_mass([{'a': 1}, {'a': 2}], 'a')[1] == 2.0
    assert max_mass([{'a': 1}, {'a': 2}, {'a': 3}], 'a')[1] == 3.0
    assert isinstance(max_mass([{'a': 1}, {'a': 2}], 'a')[1], float) == True
def test_max_mass_exceptions():
    with pytest.raises(ValueError):
        max_mass([{'a': ''}, {'a': ''}], 'a')           # empty values for all dictionaries
    with pytest.raises(KeyError):
        max_mass([{'a': 1}, {'a': 2}], 'b')             # key not in dicts

def test_min_mass():
    assert min_mass([{'a': 1}], 'a')[1] == 1.0
    assert min_mass([{'a': 1}, {'a': 2}], 'a')[1] == 1.0
    assert min_mass([{'a': 1}, {'a': 2}, {'a': 3}], 'a')[1] == 1.0
    assert isinstance(min_mass([{'a': 1}, {'a': 2}], 'a')[1], float) == True
def test_max_mass_exceptions():
    with pytest.raises(ValueError):
        min_mass([{'a': ''}, {'a': ''}], 'a')           # empty values for all dictionaries
    with pytest.raises(KeyError):
        min_mass([{'a': 1}, {'a': 2}], 'b')             # key not in dicts

