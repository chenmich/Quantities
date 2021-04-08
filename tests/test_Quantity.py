import pytest
from math import isclose

from quantities import length
from quantities import velocity
from quantities.quantity import Quantity

def test_Quantity_add_substract():
    l_type = length.LengthType
    l1 = length.Length(22, unit=l_type.k_unit)
    l2 = length.Length(33, unit=l_type.m_unit)    
    v = velocity.Velocity(3)

    l3 = l1.add(l2)
    assert l3.q_type == l_type
    assert l3.current_unit == l_type.SI_conherent_unit
    assert isclose(l3.value, 22000.033)
    with pytest.raises(ValueError):
        l1.add(None)
    with pytest.raises(ValueError):
        l1.add(42)
    with pytest.raises(ValueError):
        l1.add(v)
    
    l4 = l1.substract(l2)
    assert l4.q_type == l_type
    assert l3.current_unit == l_type.SI_conherent_unit
    assert isclose(l4.value, 22000-0.033)
    with pytest.raises(ValueError):
        l1.substract(None)
    with pytest.raises(ValueError):
        l1.substract(42)
    with pytest.raises(ValueError):
        l1.substract(v)
def test_Quantity_to_unit():
    l = length.Length(22000)
    l1 = l.to_unit(l.q_type.k_unit)

    assert l.q_type == l1.q_type
    assert isclose(l.value /1000, l1.value)
    assert l1.current_unit == l.q_type.k_unit
    with pytest.raises(TypeError):
        l.to_unit(velocity.VelocityType.k_unit)
    with pytest.raises(TypeError):
        l.to_unit(int)
    with pytest.raises(TypeError):
        l.to_unit(None)
def test_Quantity_create():
    q_type = length.LengthType
    q = Quantity(32, q_type, length.LengthType.k_unit)
    assert q.value == 32
    assert q.q_type == q_type
    assert q.current_unit in length.LengthType.__dict__.values()

    with pytest.raises(TypeError):
        Quantity(32, q_type, velocity.VelocityType.k_unit)
    with pytest.raises(TypeError):
        Quantity(32, q_type, int)

    q1 = Quantity(32, q_type)
    assert q1.value == 32
    assert q1.q_type == q_type
    assert q1.current_unit == q.q_type.SI_conherent_unit
    
    