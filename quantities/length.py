from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit

class m(Unit):
    pass

class LengthType(QuantityType):
    pri_unit = m
    SI_conherent_unit = pri_unit
    @classmethod
    def regist_type(cls):
        pass

class Length(Quantity):
    def __init__(self, value:float, unit=None):
        super().__init__(value, LengthType, unit)
        

    