from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .volume import VolumeType
from .amount_of_substance import AmountOfSubstanceType

class mole_per_cubic_meter(Unit):
    profile = {
        "name":"ampere per  meter",
        "symbol":"",
        "express_by_SI_base":"mol*m-3",
        "express_by_SI":""
    }

class AmountOfSubstanceConcentrationType(QuantityType):
    pri_unit = mole_per_cubic_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(AmountOfSubstanceType, '/', VolumeType)] = cls
        cls.source[(cls, '*', VolumeType)] = AmountOfSubstanceType
        cls.source[(VolumeType, '*', cls)] = AmountOfSubstanceType
        cls.source[(AmountOfSubstanceType, '/', cls)] = VolumeType

class AmountOfSubstanceConcentration(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, AmountOfSubstanceConcentrationType, Unit)