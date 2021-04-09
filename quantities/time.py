from .quantity_type import QuantityType
from .quantity import Quantity

from .units import Unit

class s(Unit):
    pass

class TimeType(QuantityType):
    pri_unit = s
    SI_conherent_unit = pri_unit
    @classmethod
    def regist_type(cls):
        pass

class Time(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, TimeType, unit)
