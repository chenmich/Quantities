import pytest
from quantities.quantity_type import QuantityType
from quantities.units import Unit
from quantities.length import LengthType, m


def test_QuantityType_create():
    assert QuantityType.pri_unit == Unit

def test_create_prefix_unit_for_LengthType():
    assert LengthType.d_unit.__name__ == 'dm'