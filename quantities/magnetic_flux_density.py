from . quantity_type import QuantityType
from . quantity import Quantity
from . units import Unit
from . magnetic_flux import MagneticFluxType
from . area import AreaType

class tesla(Unit):
    profile = {
        "name":"tesla",
        "symbol":"T",
        "express_by_SI_base":"kg*s-22*A-1",
        "express_by_SI":"Wb/m+2"
    }
class MagneticFluxDensityType(QuantityType):
    pri_unit = tesla
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(MagneticFluxType, '/', AreaType)] = cls
        cls.source[(cls, '*', AreaType)] = MagneticFluxType
        cls.source[(AreaType, '*', cls)] = MagneticFluxType

class MagneticFluxDensity(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, MagneticFluxDensityType, unit)


