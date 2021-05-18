from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit

class cd(Unit):
    profile = {
        "name":"candela",
        "symbol":"cd",
        "express_by_SI_base":"cd", 
        "express_by_SI":"cd"
    }

class LuminousIntensityType(QuantityType):
    pri_unit = cd
    pri_unit
    @classmethod
    def register_type(cls):
        pass

class LuminousIntensity(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, LuminousIntensityType, unit)