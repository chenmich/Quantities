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
class litre(Unit):
    profile = {
        "name":"litre",
        "symbol":"l",
        "express_by_SI_base":"",
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return value / 1e+3
    @classmethod
    def from_pri_unit(cls, value):
        return value * 1e+3

class gallon(Unit):
    profile = {
        "name":"gallon",
        "symbol":"gal",
        "express_by_SI_base":"",
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return 0.0037854117840007 * value
    @classmethod
    def from_pri_unit(cls, value):
        return value / 0.0037854117840007

class VolumeType(QuantityType):
    pri_unit = cubic_meter
    SI_conherent_unit = pri_unit
    litre = litre
    gallon = gallon
    @classmethod
    def register_type(cls):
        cls.source[(LengthType, '*', AreaType)] = cls
        cls.source[(AreaType, '*', LengthType)] = cls
        cls.source[(cls, '/', LengthType)] = AreaType
        cls.source[(cls, '/', AreaType)] = LengthType

class Volume(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, VolumeType, unit)