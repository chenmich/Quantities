from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .length import LengthType
from .radial_length import RadialLengthType
class square_meter(Unit):
    profile = {
        "name":"meter",
        "symbol":"", 
        "express_by_SI_base":"m+2", 
        "express_by_SI":""
    }

class hectare(Unit):
    profile = {
        "name":"hectare",
        "symbol":"ha", 
        "express_by_SI_base":"m+2", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return 1e+4 * value
    @classmethod
    def from_pri_unit(cls, value):
        return value / 1e+4
class AreaType(QuantityType):
    pri_unit = square_meter
    SI_conherent_unit = pri_unit
    hectare = hectare
    @classmethod
    def register_type(cls):
        cls.source[(LengthType, '*', LengthType)] = cls
        cls.source[(cls, '/', LengthType)] = LengthType

class Area(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, AreaType, unit)

