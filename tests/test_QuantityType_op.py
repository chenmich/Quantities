import pytest
from quantities import quantity
from quantities import length
from quantities import time
from quantities import velocity

def test_QuantityType_multiply_divide():
    v_type = velocity.VelocityType
    l_type = length.LengthType
    t_type = time.TimeType 

    assert l_type == v_type.multiply(t_type)
    assert l_type == t_type.multiply(v_type)
    assert v_type == l_type.divide(t_type)
    assert t_type == l_type.divide(v_type)

    with pytest.raises(TypeError):
        l_type.multiply(v_type)
    with pytest.raises(TypeError):
        l_type.multiply(None)
    with pytest.raises(TypeError):
        l_type.multiply(int)    
    with pytest.raises(TypeError):
        l_type.divide(None)
    with pytest.raises(TypeError):
        l_type.divide(str)
    
    with pytest.raises(TypeError):
        v_type.multiply(l_type)
    with pytest.raises(TypeError):
        v_type.multiply(None)
    with pytest.raises(TypeError):
        v_type.multiply(float)
    with pytest.raises(TypeError):
        v_type.divide(l_type)
    with pytest.raises(TypeError):
        v_type.divide(l_type)
    with pytest.raises(TypeError):
        v_type.divide(float)
    with pytest.raises(TypeError):
        v_type.divide(None)

    with pytest.raises(TypeError):
        t_type.multiply(l_type)
    with pytest.raises(TypeError):
        t_type.multiply(None)
    with pytest.raises(TypeError):
        t_type.multiply(float)
    with pytest.raises(TypeError):
        t_type.divide(l_type)
    with pytest.raises(TypeError):
        t_type.divide(dict)
    with pytest.raises(TypeError):
        t_type.divide(None)


def test_QuantityType_add_substract():
    l_type = length.LengthType
    v_type = velocity.VelocityType
    with pytest.raises(TypeError):
        l_type.add(v_type)
    with pytest.raises(TypeError):
        l_type.substract(v_type)
    with pytest.raises(TypeError):
        l_type.add(float)
    with pytest.raises(TypeError):
        l_type.substract(None)
    