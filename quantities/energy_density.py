from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .energy import EnergyType
from .volume import VolumeType

class joule_per_cubic_meter(Unit):
    profile = {   
        "name":"joule per cubic meter",
        "symbol":"J*m-3",
        "express_by_SI_base":"kg*m-1*s-2",
        "express_by_SI":""
    }

class EnergyDensityType(QuantityType):
    pri_unit = joule_per_cubic_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(EnergyType, '/', VolumeType)] = cls
        cls.source[(cls, '*', VolumeType)] = EnergyType
        cls.source[(VolumeType, '*', cls)] = EnergyType
        cls.source[(EnergyType, '/', cls)] = VolumeType

class EnergyDensity(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, EnergyDensityType, unit)
