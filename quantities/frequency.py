from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .time import TimeType
from .identity import IdentityType

class hertz(Unit):
    profile = {
        "name":"hertz",
        "symbol":"Hz",
        "express_by_SI_base":"s-1",
        "express_by_SI":""
    }

class FrequencyType(QuantityType):
    pri_unit = hertz
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(IdentityType, '/', TimeType)] = cls
        cls.source[(cls, '*', TimeType)] = IdentityType
        cls.source[(TimeType, '*', cls)] = IdentityType
        cls.source[(IdentityType, '/', cls)] = TimeType

class Frequency(Quantity):
    def __init__(self, value, unit):
        super().__init__(value, FrequencyType, unit)
