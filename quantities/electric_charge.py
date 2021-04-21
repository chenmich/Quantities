from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .electric_current import ElectriCurrentType
from .time import TimeType

class coulomb(Unit):
    profile = {
        "name":"coulomb",
        "symbol":"C",
        "express_by_SI_base":"A*s",
        "express_by_SI":""
    }
class ElectriChargeType(QuantityType):
    pri_unit = coulomb
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(ElectriCurrentType, '*', TimeType)] = cls
        cls.source[(cls, '/', TimeType)] = ElectriCurrentType

class ElectriCharge(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, ElectriChargeType, unit)