from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit

class K(Unit):
    profile = {
        "name":"kelvin",
        "symbol":"K",
        "express_by_SI_base":"K", 
        "express_by_SI":"K"
    }

class ThermodynamicTemperatureType(QuantityType):
    pri_unit = K
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        pass

class ThermodynamicTemperature(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, ThermodynamicTemperatureType, unit)