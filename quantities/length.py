from .quantity_type import QuantityType
from .units import Unit

class m(Unit):
    pass

class LengthType(QuantityType):
    pri_unit = m
    SI_conherent_unit = pri_unit
    @classmethod
    def regist_type(cls):
        pass

    