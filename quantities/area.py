from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .length import LengthType, RadialLengthType

class square_meter(Unit):
    profile = {
        "name":"meter",
        "symbol":"", 
        "express_by_SI_base":"m+2", 
        "express_by_SI":""
    }

class AreaType(QuantityType):
    pri_unit = square_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def regist_type(cls):
        cls.source[(LengthType, '*', LengthType)] = cls
        cls.source[(cls, '/', LengthType)] = LengthType

class Area(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, AreaType, unit)

class RadialAreaType(QuantityType):
    pri_unit = square_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def regist_type(cls):
        cls.source[(RadialLengthType, '*', RadialLengthType)] = cls
        cls.source[(cls, '/', RadialLengthType)] = RadialLengthType