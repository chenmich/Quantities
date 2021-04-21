from . quantity_type import QuantityType
from . quantity import Quantity
from . units import Unit
from . mass import MassType
from . volume import VolumeType

class kilogram_per_cubic_meter(Unit):
    profile = {
        "name":"kilogram per cubic meter",
        "symbol":"",
        "express_by_SI_base":"kg*m-3",
        "express_by_SI":""
    }

class DensityType(QuantityType):
    pri_unit = kilogram_per_cubic_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(MassType, '/', VolumeType)] = cls
        cls.source[(VolumeType, '*', cls)] = MassType
        cls.source[(cls, '*', VolumeType)] = MassType
class Density(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, DensityType, unit)