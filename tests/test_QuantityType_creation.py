import pytest
from quantities.quantity_type import QuantityType
from quantities.units import Unit
from quantities.length import LengthType, m
from quantities.time import TimeType, s


def test_QuantityType_create():
    assert QuantityType.pri_unit == Unit

def test_create_prefix_unit_for_LengthType():
    assert LengthType.d_unit.__name__ == 'dam'
    assert LengthType.SI_conherent_unit == LengthType.pri_unit
    assert TimeType.d_unit.__name__ == 'das'
    assert TimeType.SI_conherent_unit == TimeType.pri_unit