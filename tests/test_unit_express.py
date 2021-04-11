import pytest
from quantities import velocity
from quantities import length
from quantities import time
from quantities import acceleration
from quantities import mass
from quantities import force



def test_unit_press():
    l = length.Length(33)
    assert l.current_unit.symbol() == "m"
    assert l.current_unit.express_by_SI_base() == ("m", "m")
    assert l.current_unit.express_by_SI() == ("m", "m")

    t = time.Time(22)
    assert t.current_unit.symbol() == 's'
    assert t.current_unit.express_by_SI_base() == ('s', "s")
    assert t.current_unit.express_by_SI() == ('s', "s")

    mass_q = mass.Mass(54)
    assert mass_q.q_type.pri_unit.symbol() == 'g','g'
    assert mass_q.q_type.pri_unit.express_by_SI_base() == ('g', 'g')
    assert mass_q.q_type.pri_unit.express_by_SI() == ('g', 'g')

    v = velocity.Velocity(73)
    assert v.current_unit.symbol() == 'm/s'
    assert v.current_unit.express_by_SI_base() == ('m/s', 'm/s')
    assert v.current_unit.express_by_SI() == ('m/s', 'm/s')

    a = acceleration.Acceleration(88)
    assert a.current_unit.symbol() == ''
    assert a.current_unit.express_by_SI_base() == (r'm\cdot s^{-2}','m·s<sup>-2</sup>')
    assert a.current_unit.express_by_SI() == ('', '')
    

    f = force.Force(93)
    assert f.current_unit.symbol() == 'N'
    assert f.current_unit.express_by_SI_base() == (r'kg\cdot m\cdot s^{-2}', 'kg·m·s<sup>-2</sup>')
    assert f.current_unit.express_by_SI() == ('','')

    
