from . import quantity_type
from . import units
from . import time
from . import quantity
from . import velocity

class meter_per_s_s(units.Unit):
    profile = {
        "name":"meter per second second",
        "symbol":"",
        "express_by_SI_base":"m*s-2",
        "express_by_SI":""
    }
class AccelerationType(quantity_type.QuantityType):
    pri_unit = meter_per_s_s
    SI_conherent_unit = pri_unit    
    @classmethod
    def register_type(cls):
        cls.source[(velocity.VelocityType, '/', time.TimeType)] = cls
        cls.source[(cls, '*', time.TimeType)] = velocity.VelocityType
        cls.source[(time.TimeType, '*', cls)] = velocity.VelocityType
        cls.source[(velocity.VelocityType, '/', cls )] = time.TimeType
class Acceleration(quantity.Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, AccelerationType, unit)