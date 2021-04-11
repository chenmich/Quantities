from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit

class g(Unit):
    profile = {
        "name":"meter",
        "symbol":"g", 
        "express_by_SI_base":"g", 
        "express_by_SI":"g"
    }

class MassType(QuantityType):
    pri_unit = g
    @classmethod
    def regist_type(cls):
        cls.SI_conherent_unit = cls.k_unit

class Mass(Quantity):
    def __init__(self, value:float, unit=None):
        super().__init__(value, MassType, unit)

