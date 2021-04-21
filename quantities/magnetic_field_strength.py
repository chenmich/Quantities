from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .magnetic_flux_density import MagneticFluxDensity
from .magnetic_permeability import MagneticPermeabilityType


class ampere_per_meter(Unit):
    profile = {
        "name":"ampere per  meter",
        "symbol":"",
        "express_by_SI_base":"A*m-1",
        "express_by_SI":""
    }

class MagneticFieldStrengthType(QuantityType):
    pri_unit = ampere_per_meter
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(MagneticFluxDensity, '/', MagneticPermeabilityType)] = cls
        cls.source[(cls, '*', MagneticPermeabilityType)] = MagneticFluxDensity
        cls.source[(MagneticPermeabilityType, '*', cls)] = MagneticFluxDensity
        cls.source[(MagneticFluxDensity, '/', cls)] = MagneticPermeabilityType
class MagneticFieldStrength(Quantity):
    def __init__(self, value, unit=None): 
        super().__init__(value, MagneticFieldStrengthType, unit)