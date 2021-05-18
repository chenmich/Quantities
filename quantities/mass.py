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
class tonne(Unit):
    profile = {
        "name":"tonne",
        "symbol":"t", 
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return value * 1000 * 1000
    @classmethod
    def from_pri_unit(cls, value):
        return value / (1000 * 1000)
class dalton(Unit):
    profile = {
        "name":"dalton",
        "symbol":"Da", 
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return value * 1.66053906660e-24
    @classmethod
    def from_pri_unit(cls, value):
        return value / 1.66053906660e-24

class MassType(QuantityType):
    pri_unit = g
    tonne = tonne
    dalton = dalton
    @classmethod
    def register_type(cls):
        cls.SI_conherent_unit = cls.k_unit

class Mass(Quantity):
    def __init__(self, value:float, unit=None):
        super().__init__(value, MassType, unit)

