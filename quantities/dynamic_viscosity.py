from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .stress import StressType
from .gradient_speed_position import GradientSpeedPositionType

class pascal_second(Unit):
    profile = {
        "name":"pascal second",
        "symbol":"Pa*s",
        "express_by_SI_base":"kg*m-1*s-1",
        "express_by_SI":""
    }

class DynamicViscosityType(QuantityType):
    pri_unit = pascal_second
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(StressType, '/', GradientSpeedPositionType)] = cls
        cls.source[(StressType, '/', cls)] = GradientSpeedPositionType
        cls.source[(cls, '*', GradientSpeedPositionType)] = StressType
        cls.source[(GradientSpeedPositionType, '*', cls)] = StressType

class DynamicViscosity(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, DynamicViscosityType, unit)