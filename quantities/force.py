from . import quantity_type
from . import units
from . import mass
from . import quantity
from . import acceleration

class N(units.Unit):
    profile = {
        "name":"newton",
        "symbol":"N",
        "express_by_SI_base":"kg*m*s-2",
        "express_by_SI":""
    }
class ForceType(quantity_type.QuantityType):
    pri_unit = N
    SI_conherent_unit = pri_unit    
    @classmethod
    def register_type(cls):
        cls.source[(mass.MassType, '*', acceleration.AccelerationType)] = cls
        cls.source[(acceleration.AccelerationType, "*", mass.MassType)] = cls
        cls.source[(cls, "/", mass.MassType)] = acceleration.AccelerationType
        cls.source[(cls, "/", acceleration.AccelerationType)] = mass.MassType
class Force(quantity.Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, ForceType, unit)