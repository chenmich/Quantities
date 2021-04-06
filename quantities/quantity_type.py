from . import units

class metaQuantityType(type):
    def __new__(cls, name, bases, classdict):
        q_type = type.__new__(cls, name, bases, classdict)
        #create the prefix unit for q_type by it's pri_unit
        if name != 'QuantityType':
            q_type.regist_type()
        return q_type


class QuantityType(metaclass=metaQuantityType):
    pri_unit = units.Unit
    SI_conherent_unit = pri_unit
    d_unit = units.dUnit
    def regist_type(cls):
        raise NotImplementedError
    