from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit

class newton_per_square_ampere(Unit):
    profile = {
        "name":"newton per square ampere",
        "symbol":"",
        "express_by_SI_base":"N*A-2",
        "express_by_SI":""
    }
class MagneticPermeabilityType(QuantityType):
    pri_unit = newton_per_square_ampere
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        pass

class MagneticPermeability(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, MagneticPermeabilityType, unit)