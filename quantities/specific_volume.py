from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .mass import MassType
from .volume import VolumeType
from .density import DensityType
from .identity import IdentityType

class cubic_meter_per_kilogram(Unit):
    profile = {
        "name":"cubic meter per kilogram",
        "symbol":"",
        "express_by_SI_base":"kg*m-2",
        "express_by_SI":""
    }

class SpecificVolumeType(QuantityType):
    pri_unit = cubic_meter_per_kilogram
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(VolumeType, '/', MassType)] = cls
        cls.source[(MassType, '*', cls)] = VolumeType
        cls.source[(cls, '*', MassType)] = VolumeType
        cls.source[(VolumeType, '/', cls)] = MassType
        cls.source[(IdentityType, '/', cls)] = DensityType
        cls.source[(IdentityType, '/', DensityType)] = cls
    
class SpecificVolume(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, SpecificVolumeType, unit)
