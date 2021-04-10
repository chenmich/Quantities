import pytest
from quantities.quantity_type import QuantityType
from quantities import units
from quantities.length import LengthType, m
from quantities.time import TimeType, s


def test_QuantityType_create():
    assert QuantityType.pri_unit == units.Unit
    assert QuantityType.SI_conherent_unit == units.Unit

def test_create_prefix_unit_for_LengthType():
    assert LengthType.da_unit.__name__ == 'dam'
    assert LengthType.h_unit.__name__  == 'hm'
    assert LengthType.k_unit.__name__  == 'km'
    assert LengthType.M_unit.__name__  == 'Mm'
    assert LengthType.G_unit.__name__  == 'Gm'
    assert LengthType.T_unit.__name__  == 'Tm'
    assert LengthType.P_unit.__name__  == 'Pm'
    assert LengthType.E_unit.__name__  == 'Em'
    assert LengthType.Z_unit.__name__  == 'Zm'
    assert LengthType.Y_unit.__name__  == 'Ym'

    assert LengthType.d_unit.__name__  == 'dm'
    assert LengthType.c_unit.__name__  == 'cm'
    assert LengthType.m_unit.__name__  == 'mm'
    assert LengthType.mu_unit.__name__ == 'mum'
    assert LengthType.n_unit.__name__  == 'nm'
    assert LengthType.p_unit.__name__  == 'pm'
    assert LengthType.f_unit.__name__  == 'fm'
    assert LengthType.a_unit.__name__  == 'am'
    assert LengthType.z_unit.__name__  == 'zm'
    assert LengthType.y_unit.__name__  == 'ym'
def test_create_prefix_unit_for_TimeType():    
    assert TimeType.da_unit.__name__ == 'das'
def test_set_relation_between_type_unit():
    LengthType.q_typ = LengthType.pri_unit.q_type
def test_create_all_prefix_units():
    assert QuantityType.da_unit == units.daUnit
    assert QuantityType.h_unit == units.hUnit

    assert QuantityType.da_unit == units.daUnit
    assert QuantityType.h_unit  == units.hUnit
    assert QuantityType.k_unit  == units.kUnit
    assert QuantityType.M_unit  == units.MUnit
    assert QuantityType.G_unit  == units.GUnit
    assert QuantityType.T_unit  == units.TUnit
    assert QuantityType.P_unit  == units.PUnit
    assert QuantityType.E_unit  == units.EUnit
    assert QuantityType.Z_unit  == units.ZUnit
    assert QuantityType.Y_unit  == units.YUnit
    
    assert QuantityType.d_unit  == units.dUnit
    assert QuantityType.c_unit  == units.cUnit
    assert QuantityType.m_unit  == units.mUnit
    assert QuantityType.mu_unit == units.muUnit
    assert QuantityType.n_unit  == units.nUnit
    assert QuantityType.p_unit  == units.pUnit
    assert QuantityType.f_unit  == units.fUnit
    assert QuantityType.a_unit  == units.aUnit
    assert QuantityType.z_unit  == units.zUnit
    assert QuantityType.y_unit  == units.yUnit