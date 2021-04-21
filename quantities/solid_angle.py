from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .area import AreaType
from .radial_area import RadialAreaType

class steradian(Unit):
    profile = {
        "name":"steradian",
        "symbol":"sr", 
        "express_by_SI_base":"m+2/m+2", 
        "express_by_SI":""
    }

class SolidAngleType(QuantityType):
    pri_unit = steradian
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(AreaType, '/', RadialAreaType)] = cls
        cls.source[(cls, '*', RadialAreaType)] = AreaType
        cls.source[(AreaType, '/', cls)] = RadialAreaType
class SolidAngle(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, SolidAngleType, unit)