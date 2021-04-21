from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .area import AreaType
from .length import LengthType

class cubic_meter(Unit):
    profile = {
        "name":"cubic meter",
        "symbol":"",
        "express_by_SI_base":"m+3",
        "express_by_SI":""
    }

class VolumeType(QuantityType):
    pri_unit = cubic_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(LengthType, '*', AreaType)] = cls
        cls.source[(AreaType, '*', LengthType)] = cls
        cls.source[(cls, '/', LengthType)] = AreaType
        cls.source[(cls, '/', AreaType)] = LengthType

class Volume(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, VolumeType, unit)