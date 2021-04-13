import pytest
from math import isclose
from quantities import identity
from quantities import length


def test_Identity_multiply_divide():
    i = identity.Identity(3, identity.IdentityType.k_unit)
    l1 = length.Length(3, length.LengthType.M_unit)
    l2 = length.Length(6, length.LengthType.d_unit)

    l3 = i.multiply(l1)
    assert isclose(l3.value, 9e+9)
    assert l3.q_type == length.LengthType    
    assert l3.current_unit == l1.q_type.SI_conherent_unit

    l4 = l2.multiply(i)
    assert isclose(l4.value, 18e+2)
    assert l4.q_type == l2.q_type
    assert l4.current_unit == length.LengthType.SI_conherent_unit

    l5 = l2.divide(i)
    assert isclose(l5.value, 2e-4)
    assert l5.q_type == l2.q_type
    assert l5.current_unit == length.LengthType.SI_conherent_unit

    l6 = i * l1
    assert l6 == l3
    l7 = l2 / i
    assert l7 == l5

    '''
    There is no division for identity, because it makes no sense
    Even if the relationship between the number 
    of frequencies and time is obtained  by dividing Identity by time, 
    the division relationship can be determined by paying attention to the number of frequencies.
    '''
    #l6 = i.divide(l2)
    #assert isclose(l6.value, 5e+5)
    #assert l6.q_type == l2.q_type
    #assert l6.current_unit == length.LengthType.SI_conherent_unit
    with pytest.raises(TypeError):
        i.divide(l2)
    
    i1 = l2.divide(l1)
    assert isclose(i1.value, 2e-7)
    assert i1.q_type == identity.IdentityType
    assert i1.current_unit == identity.IdentityUnit

    i2 = l2 / l1
    assert i1 == i2
    with pytest.raises(TypeError):
        i / l2