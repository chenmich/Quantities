'''
Generally, if a physical quantity is divided by itself, 
the physical quantity obtained should be the Identity quantity. 
However, the plane angle is a physical quantity obtained by dividing the length by the length. 
It has a clear geometric and physical meaning, 
and it cannot be simply regarded as an Identity quantity. 
In order to distinguish them in the class library, 
it is necessary to distinguish the two physical quantities expressing the angle. 
In fact, these two physical quantities are also different. 
As the length of the dividend, it is the length of the arc on the plane stretched by the angle, 
and as the divisor, it is the length of the radius of the arc. The two are geometrically different. 
Therefore, borrow their differences in the design of the class library 
to achieve the type of calculation of physical quantities. 
For solid angles, Moment of force, etc., there are also such issues that need to be dealt with. 
Therefore, the classes RadialLength and RadialAreaType are specially designed in the class library 
to solve such problems.
'''
import math
from .quantity_type import QuantityType
from .quantity import Quantity
from .units import Unit
from .length import LengthType
from .radial_length import RadialLengthType



class radian(Unit):
    profile = {
        "name":"radian",
        "symbol":"rad", 
        "express_by_SI_base":"m/m", 
        "express_by_SI":""
    }
class degree(Unit):
    profile = {
        "name":"degree",
        "symbol":"°", 
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return (math.pi / 180) * value
    def from_pri_unit(cls, value):
        return (180 / math.pi) * value
class minute(Unit):
    profile = {
        "name":"minute",
        "symbol":"'", 
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return (math.pi / 10800) * value
    def from_pri_unit(cls, value):
        return (10800 / math.pi) * value

class second(Unit):
    profile = {
        "name":"second",
        "symbol":'''"''', 
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return (math.pi / 648000) * value
    def from_pri_unit(cls, value):
        return (648000 / math.pi) * value


class PlaneAngleType(QuantityType):
    pri_unit = radian
    SI_conherent_unit = pri_unit
    degree = degree
    minute = minute
    second = second
    @classmethod
    def register_type(cls):
        cls.source[(LengthType, '/', RadialLengthType)] = cls
        cls.source[(cls, '*', RadialLengthType)] = LengthType
        cls.source[(LengthType, '/', cls)] = RadialLengthType

class PlaneAngle(Quantity):
    def __init__(self, value, unit=None):
        super().__init__(value, PlaneAngleType, unit)
        