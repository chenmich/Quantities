from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .length import LengthType
from .identity import Identity

class per_meter(Unit):
    profile = {
        "name":"per meter",
        "symbol":"",
        "express_by_SI_base":"m-1",
        "express_by_SI":""
    }

class WavenumberType(QuantityType):
    pri_unit = per_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(Identity, '/', LengthType)] = cls
        cls.source[(cls, '*', LengthType)] = Identity
        cls.source[(LengthType, '*', cls)] = Identity

class Wavenumber(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, WavenumberType, unit)
    