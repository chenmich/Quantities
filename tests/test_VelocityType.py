from quantities import velocity
from quantities import length
from quantities import time
from quantities import quantity_type

def test_regist_q_type():
    v_type = velocity.VelocityType
    l_type = length.LengthType
    t_type = time.TimeType
    base_type = quantity_type.QuantityType
    divided_type = base_type.source[(l_type, '/', t_type)]
    multiplied_type = base_type.source[(v_type, '*', t_type)]
    another_multiplied_type = base_type.source[(t_type, '*', v_type)]
    assert divided_type == v_type
    assert multiplied_type == l_type
    assert another_multiplied_type == l_type
    assert t_type == l_type.divide(v_type)


    