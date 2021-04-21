from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .time import TimeType
from .angular_velocity import AngularVelocityType

class radian_per_second_squared(Unit):
    profile = {   
        "name":"radian per second squared",
        "symbol":"rad*s-2",
        "express_by_SI_base":"s-2",
        "express_by_SI":""
    }

class AngulaAccelerationType(QuantityType):
    pri_unit = radian_per_second_squared
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(AngularVelocityType, '/', TimeType)] = cls
        cls.source[(cls, '*', TimeType)] = AngularVelocityType
        cls.source[(TimeType, '*', cls)] = AngularVelocityType
        cls.source[(AngularVelocityType, '/', cls)] = TimeType
class AngulaAcceleration(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, AngulaAccelerationType, unit)