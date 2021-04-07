import pytest
from math import isclose
from quantities.quantity_type import QuantityType

def test_prefix_unit_convert():
    assert isclose(QuantityType.d_unit.from_pri_unit(), 1e-1)
    assert isclose(QuantityType.d_unit.to_pri_unit(), 1e+1)