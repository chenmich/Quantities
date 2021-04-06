from . import units
from . import quantity_type as baseType
class metaQuantityType(type):
    def __new__(cls, name, bases, classdict):
        q_type = type.__new__(cls, name, bases, classdict)
        #create the prefix unit for q_type by it's pri_unit
        if name != 'QuantityType':
            base_da_m = baseType.QuantityType.d_unit
            da_m = type('dam', (base_da_m,), {})
            q_type.d_unit = da_m
            q_type.regist_type()
        return q_type


class QuantityType(metaclass=metaQuantityType):
    pri_unit = units.Unit
    SI_conherent_unit = pri_unit
    d_unit = units.dUnit
    @classmethod
    def regist_type(cls):
        raise NotImplementedError
    