import pytest
from math import isclose
from quantities import length

def test_non_SI_unit():
    l = length.Length(32)
    l1 = l.to_unit(length.foot)
    l2 = l.to_unit(length.LengthType.inch)
    l3 = l.to_unit(length.LengthType.yard)
    l4 = l.to_unit(length.LengthType.mile)
    l5 = l.to_unit(length.LengthType.astronomical_unit)

    assert isclose(l1.value, 32 * 100 / 2.54 / 12)
    assert l1.current_unit == length.foot

    assert isclose(l2.value, 32 * 100 / 2.54)
    assert l2.current_unit == length.inch

    assert isclose(l3.value, 32 * 1.0936)
    assert l3.current_unit == length.yard

    assert isclose(l4.value, 32 / 1609.34)
    assert l4.current_unit == length.mile

    assert isclose(l5.value, 32 / 149597870700)
    assert l5.current_unit == length.astronomical_unit

