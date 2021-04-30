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
        from .identity import IdentityType
        if isinstance(other, (int, float,)):
            value = self.value * other
            current_unit = self.current_unit
            return Quantity(value, self.q_type, current_unit)
        if not hasattr(other, 'q_type'):
            raise ValueError("These two physical quantities can not be multiplied not!")
        elif self.q_type == IdentityType:
            q_type = other.q_type
        elif other.q_type == IdentityType:
            q_type = self.q_type
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
        '''
            This function is for true divide
        '''
        from .identity import IdentityType
        if isinstance(other, (int, float,)):
            value = self.value / other
            current_unit = self.current_unit
            return Quantity(value, self.q_type, current_unit)
        if not hasattr(other, 'q_type'):
            raise ValueError("These two physical quantities can not be divided not!")
        elif other.q_type == IdentityType:
            q_type = self.q_type
        elif self.q_type == other.q_type:
            q_type = IdentityType
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
            to_pri_value = self.current_unit.to_pri_unit(self.__value)
            value = unit.from_pri_unit(to_pri_value)
            return Quantity(value, self.q_type, unit)
    def equal(self, other):
        if not hasattr(other, 'q_type'):
            raise ValueError("These two physical quantities can not be compared now!")
        elif other.q_type != self.q_type:
            raise TypeError("The two physical quantities are of different types!")
        other_converted = other.to_unit(self.current_unit)
        return isclose(self.value, other_converted.value)
    def le(self, other):
        if not hasattr(other, 'q_type'):
            raise ValueError("These two physical quantities can not be compared now!")
        elif other.q_type != self.q_type:
            raise TypeError("The two physical quantities are of different types!")
        other_converted = other.to_unit(self.current_unit)
        return self.value <= other_converted.value
    def ge(self, other):
        if not hasattr(other, 'q_type'):
            raise ValueError("These two physical quantities can not be compared now!")
        elif other.q_type != self.q_type:
            raise TypeError("The two physical quantities are of different types!")
        other_converted = other.to_unit(self.current_unit)
        return self.value >= other_converted.value
    def lt(self, other):
        if not hasattr(other, 'q_type'):
            raise ValueError("These two physical quantities can not be compared now!")
        elif other.q_type != self.q_type:
            raise TypeError("The two physical quantities are of different types!")
        other_converted = other.to_unit(self.current_unit)
        return self.value < other_converted.value
    def gt(self, other):
        if not hasattr(other, 'q_type'):
            raise ValueError("These two physical quantities can not be compared now!")
        elif other.q_type != self.q_type:
            raise TypeError("The two physical quantities are of different types!")
        other_converted = other.to_unit(self.current_unit)
        return self.value > other_converted.value
    def __eq__(self, other):
        return self.equal(other)
    def __le__(self, other):
        return self.le(other)
    def __ge__(self, other):
        return self.ge(other)
    def __gt__(self, other):
        return self.gt(other)
    def __lt__(self, other):
        return self.lt(other)
    def __hash__(self):
        return hash((self.q_type, self.value, self.current_unit))
    def __mul__(self, other):
        return self.multiply(other)
    def __truediv__(self, other):
        return self.divide(other)
    def __rmul__(self, other):
        return self.multiply(other)
    @property
    def value(self):
        return self.__value
    @property
    def current_unit(self):
        return self.__unit
    @property
    def q_type(self):
        return self.__type
    
        

