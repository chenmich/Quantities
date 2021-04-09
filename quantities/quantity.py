from math import isclose
from .quantity_type import QuantityType
from .units import Unit

class Quantity():
    def __init__(self, value:float, q_type:QuantityType, unit=None):
        self.__value = value
        self.__type = q_type
        if unit not in self.__type.__dict__.values():
            raise TypeError("The unit is not one of the units of quantity' q_type!")
        if unit != None:
            self.__unit = unit        
        else:
            self.__unit = q_type.SI_conherent_unit
    def add(self, other):
        if not hasattr(other, 'q_type') or other.q_type != self.q_type:
            raise ValueError("These two physical quantities can not be added now!")
        other_by_current_unit = other.to_unit(self.current_unit)
        value = self.value + other_by_current_unit.value
        return Quantity(value, self.q_type, unit=self.current_unit).to_unit(self.q_type.SI_conherent_unit)
        
    def substract(self, other):
        if not hasattr(other, 'q_type') or other.q_type != self.q_type:
            raise ValueError('These two physical quantities can not be substracted now! ')
        other_by_current_unit = other.to_unit(self.current_unit)
        value = self.value - other_by_current_unit.value
        return Quantity(value, self.q_type, unit=self.current_unit).to_unit(self.q_type.SI_conherent_unit)
    def multiply(self, other):
        if not hasattr(other, 'q_type'):
            raise ValueError("These two physical quantities can not be multiplied not!")
        else:
            try:
                q_type = self.q_type.multiply(other.q_type)
            except TypeError as exc:
                raise TypeError("These types of two physical quantities can not be multiplied not!") from exc
        other_converted = other.to_unit(other.q_type.SI_conherent_unit)
        self_converted = self.to_unit(self.q_type.SI_conherent_unit)
        value = self_converted.value * other_converted.value
        return Quantity(value, q_type)
        
    def divide(self, other):
        if not hasattr(other, 'q_type'):
            raise ValueError("These two physical quantities can not be divided not!")
        else:
            try:
                q_type = self.q_type.divide(other.q_type)
            except TypeError as exc:
                raise TypeError("These types of two physical quantities can not be divided not!") from exc
        other_converted = other.to_unit(other.q_type.SI_conherent_unit)
        self_converted = self.to_unit(self.q_type.SI_conherent_unit)
        value = self_converted.value / other_converted.value
        return Quantity(value, q_type)
    def to_unit(self, unit:Unit):
        if unit not in self.q_type.__dict__.values() or unit == None:
            raise TypeError('The unit is not for this physical qunatity!')
        else:
            to_pri_coffic = self.current_unit.to_pri_unit()
            from_pri_coffic = unit.from_pri_unit()
            value = self.value * to_pri_coffic * from_pri_coffic
            return Quantity(value, self.q_type, unit)
    def equal(self, other):
        if not hasattr(other, 'q_type'):
            raise ValueError("These two physical quantities can not be compared now!")
        elif other.q_type != self.q_type:
            raise TypeError("The two physical quantities are of different types!")
        other_converted = other.to_unit(self.current_unit)
        return isclose(self.value, other_converted.value)

    @property
    def value(self):
        return self.__value
    @property
    def current_unit(self):
        return self.__unit
    @property
    def q_type(self):
        return self.__type
    
        

