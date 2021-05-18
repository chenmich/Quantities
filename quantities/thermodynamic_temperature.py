from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit

class K(Unit):
    profile = {
        "name":"kelvin",
        "symbol":"K",
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
class celsius_degree(Unit):
    profile = {
        "name":"celsius degree",
        "symbol":"°",
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return value + 273.15
    @classmethod
    def from_pri_unit(cls, value):
        return value - 273.15
class fahrenheit_degree(Unit):
    profile = {
        "name":"fahrenheit degree",
        "symbol":"F",
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return (5 / 9) * (value - 32) + 273.15
    @classmethod
    def from_pri_unit(cls, value):
        return (9 / 5) * (value -273.15) + 32
class ThermodynamicTemperatureType(QuantityType):
    pri_unit = K
    SI_conherent_unit = pri_unit
    celsius_degree =  celsius_degree
    fahrenheit_degree = fahrenheit_degree
    @classmethod
    def register_type(cls):
        pass

class ThermodynamicTemperature(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, ThermodynamicTemperatureType, unit)