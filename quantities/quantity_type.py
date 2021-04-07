from . import units
from . import quantity_type as baseType
class metaQuantityType(type):
    def __new__(cls, name, bases, classdict):
        q_type = type.__new__(cls, name, bases, classdict)
        #create the prefix unit for q_type by it's pri_unit
        if name != 'QuantityType':
            prefix_name_value = units.__prefix_value__.copy()
            del prefix_name_value['base']
            for prefix in prefix_name_value.keys():
                base_da_m = getattr(baseType.QuantityType, prefix + '_unit')
                prefix_unit_name = prefix + q_type.pri_unit.__name__
                prefix_unit = type(prefix_unit_name, (base_da_m,), {})
                setattr(q_type, prefix+"_unit", prefix_unit)
            q_type.regist_type()
        return q_type


class QuantityType(metaclass=metaQuantityType):
    source = {}
    pri_unit = units.Unit
    SI_conherent_unit = pri_unit
    da_unit = units.daUnit
    h_unit  = units.hUnit
    k_unit  = units.kUnit
    M_unit  = units.MUnit
    G_unit  = units.GUnit
    T_unit  = units.TUnit
    P_unit  = units.PUnit
    E_unit  = units.EUnit
    Z_unit  = units.ZUnit
    Y_unit  = units.YUnit

    d_unit  = units.dUnit
    c_unit  = units.cUnit
    m_unit  = units.mUnit
    mu_unit = units.muUnit
    n_unit  = units.nUnit
    p_unit  = units.pUnit
    f_unit  = units.fUnit
    a_unit  = units.aUnit
    z_unit  = units.zUnit
    y_unit  = units.yUnit
    @classmethod
    def regist_type(cls):
        raise NotImplementedError
    @classmethod
    def divide(cls, other):
        try:
            divided_type = cls.source[(cls, '/', other)]
        except KeyError as exc:
            raise TypeError("The two qunatity can not be divide now!") from exc
        return divided_type
    @classmethod
    def multiply(cls, other):
        try:
            multiplied_type = cls.source[(cls, '*', other)]
        except KeyError as exc:
            raise TypeError("The two qunatity can not be multiply now!") from exc
        return multiplied_type