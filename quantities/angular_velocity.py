from .quantity import Quantity
from .quantity_type import QuantityType
from .units import Unit
from .plane_angle import PlaneAngleType
from .time import TimeType

class radian_per_second(Unit):
    profile = {   
        "name":"radian per second",
        "symbol":"rad*s-1",
        "express_by_SI_base":"s-1",
        "express_by_SI":""
    }

class AngularVelocityType(QuantityType):
    pri_unit = radian_per_second
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(PlaneAngleType, '/', TimeType)] = cls
        cls.source[(PlaneAngleType, '/', cls)] = TimeType
        cls.source[(cls, '*', TimeType)] = PlaneAngleType
        cls.source[(TimeType, '*', cls)] = PlaneAngleType

class AngularVelocity(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, AngularVelocityType, unit)
