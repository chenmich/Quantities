# Add A New Quantity

Adding a new quantity is very simple, you need to inherit two new classes from the two classes QuantityType and Unit. The former expresses a new type of physical quantity, and the latter expresses a new unit corresponding to the type of physical quantity.Detailed examples can be found in the design of [mass](https://github.com/chenmich/Quantities/blob/master/quantities/mass.py) and [energy](https://github.com/chenmich/Quantities/blob/master/quantities/energy.py).

## Designing new SI unit class

Add an new unit class is very simple. The code is as following:

```python

class joule(Unit):
    profile = {
        "name":"joule",
        "symbol":"J",
        "express_by_SI_base":"kg*m+2*s-2",
        "express_by_SI":"N*m"
    }
```

This class is the primary class of the physical quantity type, and other unit classes are related to this class. For example, it is the basis for automatically generating prefix unit classes, and it is also a transitional unit class for unit conversion. Most of the time, it is the coherent unit of the SI unit system. But there are exceptions. For example, in the unit of mass, g is the primary unit, but it is not the coherent unit selected by SI unit system. The coherent unit is kg.

For the unit class added in the new design, Physical Quantity Calculating does not know its name, symbol, and how to express it in the basic unit of the SI unit system and the derived unit with a specific name, so it needs to provide a reference when designing. This reference is placed in its class variable profile. It needs to be set as a dict object. Its four keys respectively represent the name and symbol of the primary unit, the expression in the basic unit, and the expression in the basic unit and the derived unit with a specific name.

The value corresponding to each key is determined by the unit. If the unit does not have this value, it is an empty string. If so, it needs to be delivered to Physical Quantity Calculating according to the following principles:

1. The name or symbol and power exponent of each unit must be separated by +, -, * and /.

2. The division sign specified by the SI unit system is still separated by the division sign, such as m/s. If the division sign is not specified, it is separated by a multiplication sign, such as kg*m in joule class.

3. A symbol and its power exponent are separated by plus and minus signs. The plus sign represents a positive power exponent, and the minus sign represents a negative power exponent. For example, m+2 in the joule class.

4. The power exponent of the previous symbol and the next symbol are separated by a multiplication sign. For example, 2*s in the joule class.

5. There must be no spaces before and after the symbol or the two expression strings.

Therefore, in the joule class, its symbol is J. And it needs to be written as kg\*m+2*s-2 when expressed in the basic unit of the SI unit system, and as N\*m when expressed in the basic unit and unit with specific name. Their real expressions would be $kg\cdot m^{2}\cdot s^{-2}$ and $N\cdot m$(This display is the display of Latex on the web page. If you use html display, it will be kg·m<sup>2</sup>·s<sup>-2</sup>). Of course, the expression method m/s stipulated by the SI unit system will still be retained.

## Design non-SI unit class

There is no fundamental difference between designing non-SI units and designing SI units. However, the conversion relationship between non-SI units and SI primary units is not necessarily a proportional relationship. For example, the relationship between the thermodynamic temperature unit kevin and celsius　degree is a linear relationship rather than a simple proportional relationship. So when designing a non-SI unit, you need to override two methods `#!python to_pri_unit` and `#!python from_pri_unit`. The following is an example.

```python
class celsius_degree(Unit):
    profile = {
        "name":"celsius degree",
        "symbol":"°",
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return value + 273.15
    @classmethod
    def from_pri_unit(cls, value):
        return value - 273.15

class fahrenheit_degree(Unit):
    profile = {
        "name":"fahrenheit degree",
        "symbol":"F",
        "express_by_SI_base":"", 
        "express_by_SI":""
    }
    @classmethod
    def to_pri_unit(cls, value):
        return (5 / 9) * (value - 32) + 273.15
    @classmethod
    def from_pri_unit(cls, value):
        return (9 / 5) * (value -273.15) + 32
```

## Design unit conversion relationship

If you want to establish a conversion relationship between each unit, the workload is huge and difficult to complete. It should be particularly pointed out here that the method of establishing the conversion between each pair of units in the Physical Quantity Calculating class library uses the analysis pattern of Martin Fowler. For details, see the pattern of Figure 3.3 in [UML Diagrams for Chapter 3 of Analysis Patterns](https://martinfowler.com/apsupp/apchap3.pdf)

## Design new quantity type

The design of a new quantity type needs to inherit the class QuantityType. For example, to design EnergyType, the code is as follows:

```python hl_lines="10 11 12"
class EnergyType(QuantityType):
    pri_unit = joule
    SI_conherent_unit = pri_unit
    @classmethod
    def register_type(cls):
        cls.source[(ForceType, '*', LengthType)] = cls
        cls.source[(LengthType, '*', ForceType)] = cls
        cls.source[(cls, '/', ForceType)] = LengthType
        cls.source[(cls, '/', LengthType)] = ForceType
    @classmethod
    def register_type(cls):
        pass
```

In the class design of this physical quantity, the first thing we have to set is its primary unit. In this EnergyType class, it is the class joule that we designed in the previous section. So we set the class variable `#!python  pri_unit` of the EnergyType class equals `#!python joule`.EnergyType will generate its corresponding prefixed unit based on this unit. Similarly, it is also a transitional unit for unit conversion. We will discuss this point below.

The second class variable that needs to be set in the EnergyType class is `#!python SI_coherent_unit`. It is the coherent unit of the SI unit. In the physical quantity of the EnergyType type, this unit is its primay. So we set `#!python SI_coherent_unit = pri_unit`. It should be noted that in the SI unit system, most of the primary units of physical quantities are consistent with the coherent units of the SI unit system. But there are exceptions. For example, the primary unit of MassType is g instead of kg. But kg is the basic unit of SI, and it is also a coherent unit.

When the class QuantityType is inherited for designing a new physical quantity type, a key class method `#!python register_type` needs to be overridden. In QuantityType, this method is designed to throw NotImplementedError, the purpose is to remind programmers who inherit this class to override this method. This method needs to determine the multiplication and division relationship between related physical quantities, and this is the basis for the automatic generation of physical quantities by Physical Quantity Calculating.

The overriding class method `#!python register_type` method determines that the quantity type can be obtained by multiplying or dividing the two other types. For example, the definition of EnergyType is the work done by force through a certain displacement, so it can be considered to be obtained by multiplying ForceType by LengthType. Therefore, in this method, the corresponding item should be added to the source dictionary of the class variable.

The key to be added to the dictionary is a tuple. The tuple consists of two classes of physical quantity types and the corresponding multiplication or division signs. For example, EnergyType is obtained by multiplying ForceType and LengthType, so its key is composed of tuples `#!python (ForceType,'*', LengthType)`. And its value is EnergyType. Therefore, when overriding the class method register_type, first add this value to the source dictionary, that is, the code:

```python hl_lines="1"
cls.source[(ForceType, '*', LengthType)] = cls
cls.source[(LengthType, '*', ForceType)] = cls
cls.source[(cls, '/', ForceType)] = LengthType
cls.source[(cls, '/', LengthType)] = ForceType
```

When overriding the register_type method, add as many meaningful operations as possible to the dictionary specified by source. For example, in the design of EnergyType, in addition to the first sentence expressing the definition of EnergyType, the second sentence also expresses its definition. The corresponding EnergyType and the division results of LengthType and ForceType are also meaningful, so write them separately into the dictionary pointed to by source. In this way, when applying Physical Quantity Calculating, when these four situations are encountered, the physical quantity type of the operation result can be determined.

In particular, it should be noted that in the design of QuantityType, the class variable source points to an empty dictionary. The source of its subclasses will also point to this dictionary. Each subclass will register for itself the result type of many operations in this dictionary. And in actual operation, the corresponding operation result type will be searched from this dictionary. Therefore, it is strictly forbidden for any subclass to set another dictionary for the source. Otherwise, even if the corresponding physical quantity type has been registered during the design, an error may still be thrown during the calculation process because it cannot be found.Details can be seen in the highlighted part of the aforementioned EnergyType design code snippet

If certain subclasses do not need to specifically register certain operations, they must also override the class method register_type to prevent NotImplemenedError from being thrown. See the design of [LengthType](https://github.com/chenmich/Quantities/blob/master/quantities/length.py).

When designing a new quantity type, it must also be associated with its non-SI units. For example, when designing the quantity type of thermodynamic temperature, it is necessary to associate the class celsius_degree and the class fahrenheit_degree. After the association, the user can call its non-SI unit through this quantity type.The details can be seen in the following example.

```python hl_lines="4 5"
class ThermodynamicTemperatureType(QuantityType):
    pri_unit = K
    SI_conherent_unit = pri_unit
    celsius_degree =  celsius_degree
    fahrenheit_degree = fahrenheit_degree
    @classmethod
    def register_type(cls):
        pass
```
