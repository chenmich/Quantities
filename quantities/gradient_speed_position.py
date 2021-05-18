from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .velocity import VelocityType
from .length import LengthType

class per_second(Unit):
    profile = {
        "name":"per second",
        "symbol":"",
        "express_by_SI_base":"s-1",
        "express_by_SI":""
    }

class GradientSpeedPositionType(QuantityType):
    pri_unit = per_second
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(VelocityType, '/', LengthType)] = cls
        cls.source[(LengthType, '*', cls)] = VelocityType
        cls.source[(cls, '*', LengthType)] = VelocityType
        cls.source[(VelocityType, '/', cls)] = LengthType

class GradientSpeedPosition(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, GradientSpeedPositionType, unit)