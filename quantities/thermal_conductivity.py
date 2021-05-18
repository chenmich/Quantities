from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .power import PowerType
from .gradient_temperature_position import GradientTemperaturePositionType

class watt_per_meter_kelvin(Unit):
    profile = {   
        "name":"watt per meter kelvin",
        "symbol":"W*m-1*K-1",
        "express_by_SI_base":"kg*m*s-3*K-1",
        "express_by_SI":""
    }

class ThermalConductivityType(QuantityType):
    pri_unit = watt_per_meter_kelvin
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(PowerType, '/', GradientTemperaturePositionType)] = cls
        cls.source[(cls, '*', GradientTemperaturePositionType)] = PowerType
        cls.source[(GradientTemperaturePositionType, '*', cls)] = PowerType
        cls.source[(PowerType, '/', cls)] = GradientTemperaturePositionType

class ThermalConductivity(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, ThermalConductivityType, unit)