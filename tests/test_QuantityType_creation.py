import pytest
from quantities.quantity_type import QuantityType
from quantities.units import Unit


def test_QuantityType_create():
    assert QuantityType.pri_unit == Unit