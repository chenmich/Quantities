'''
All the class are designed for stress and pressure quantity
'''

from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .area import AreaType
from .force import ForceType

class pascal(Unit):
    profile = {
        "name":"pascal",
        "symbol":"Pa",
        "express_by_SI_base":"kg*m-1*s-2",
        "express_by_SI":""
    }

class StressType(QuantityType):
    pri_unit = pascal
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(ForceType, '/', AreaType)] = cls
        cls.source[(cls, '*', AreaType)] = ForceType
        cls.source[(AreaType, '*', cls)] = ForceType
        cls.source[(ForceType, '/', cls)] = AreaType

class Stress(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, StressType, unit)