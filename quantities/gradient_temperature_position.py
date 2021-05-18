from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .length import LengthType
from .thermodynamic_temperature import ThermodynamicTemperatureType

class kelvin_per_meter(Unit):
    profile = {   
        "name":"kelvin per meter",
        "symbol":"K*m-1",
        "express_by_SI_base":"K*m-1",
        "express_by_SI":""
    }

class GradientTemperaturePositionType(QuantityType):
    pri_unit = kelvin_per_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(ThermodynamicTemperatureType, '/', LengthType)] = cls
        cls.source[(cls, '*', LengthType)] = ThermodynamicTemperatureType
        cls.source[(LengthType, '*', cls)] = ThermodynamicTemperatureType
        cls.source[(ThermodynamicTemperatureType, '/', cls)] = LengthType

class GradientTemperaturePosition(Quantity):
    def __init__(self, value, unit=None):
        super.__init__(value, GradientTemperaturePositionType, unit)