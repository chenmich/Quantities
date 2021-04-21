from . quantity import Quantity
from . quantity_type import QuantityType
from . units import Unit


class weber(Unit):
    profile = {
        "name":"weber",
        "symbol":"Wb",
        "express_by_SI_base":"kg*m+2*s-2*A-1",
        "express_by_SI":"V*s"
    }

class MagneticFluxType(QuantityType):
    pri_unit = weber
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        pass

class MagneticFlux(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, MagneticFluxType, unit)