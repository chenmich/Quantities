# API Reference

The API of Physical Quantity Calculating mainly includes the arithmetic and comparison of Quantity class, as well as the operation of transforming units such as `#!python to_unit`. We also need to pay special attention to the `#!python register` method of QuantityType. The methods of the Unit class are also very interesting, involving unit conversion and unit writing expression.

## API of the Quantity class

Quantity is the main class for programming to operate, and it is the base class for all physical quantities。It has arithmetic operations and comparison operations, in particular it also has conversion unit operations, these operations realize the calculation of the number and the conversion of units. It is an operation that is often used in programming.

### Arithmetic operations

**Quantity.add(self, other)**:　This method provides operation of the same type of physical quantity. If the parameter other is not of the same type, a ValueError exception will be thrown.　The method returns a physical quantity whose type is the same as the type of the physical quantity participating in the operation. The unit is the SI coherent unit of the physical quantity.

**Quantity.substract(self, other)**:　This method provides  operation of the same type of physical quantity. If the parameter other is not of the same type, a ValueError exception will be thrown. The method returns a physical quantity whose type is the same as the type of the physical quantity participating in the operation. The unit is the SI coherent unit of the physical quantity.

**Quantity.multiply(self, other)**:　This method returns the product of the physical quantity and other types of parameters. The system will Can return diversified results.

1. If the parameter other is of type float or int, the return result is a physical quantity whose type is the same as this physical quantity, and the unit is the same as this physical quantity, except that its value is equal to the result of multiplying the value of this physical quantity with other.
2. When other is an ohter non-Quantity type, a ValueError exception will be thrown
3. When ohter is a subtype Identity of Quantity, or when the physical quantity is Identity, the returned result is the same as the first case.
4. If other is of type Quantity or its subtypes, but the system cannot determine the type after multiplication, it will throw TypeError exception.

The following is an example of the application. Please carefully observe the running results of this example program.

```python
from quantities import length
from quantities import identity
from quantities import time
from quantities import velocity


l = length.Length(32, unit=length.LengthType.mu_unit)
i = identity.Identity(24)
v = velocity.Velocity(32)
t = time.Time(12)
l1 = l.multiply(24)
l2 = l.multiply(i)
l3 = v.multiply(t)


print(l1.value)
print(l1.current_unit.symbol())
print(l2.value)
print(l2.current_unit.symbol())
print(l3.value)
print(l3.current_unit.symbol())
try:
    l.multiply(v)
except TypeError:
    print("A TypeError is thrown!")
```

The running results of the program are as follows:

```python
768
('\\mu m', 'μm')
0.000768
('m', 'm')
384.0
('m', 'm')
A TypeError is thrown!
```

l1 is an result of the length quantity multiplied by an integer, so it is still a length quantity, and its current unit is still μm. And l2 is an result of the length quantity multiplied by an instance of the Identity quantity, the it is still the length quantity, but its unit is the SI coherent unit of this quantity. We provide an interface for multiplying integers or floating-point numbers, but we still recommend using a physical quantity to multiply an instance of Identity, so that the physical concept is clearer.

**Quantity.\__mul__(self, other)**  
**Quantity.\__rmul__(self, other)**

These two functions are magic methods of the python class, which also express multiplication, and the```#!python __rmul__()``` method expresses the concept of right multiplication. With these two functions, we can write the following code:

```python
from quantities import length
from quantities import identity
from quantities import time
from quantities import velocity


l = length.Length(32, unit=length.LengthType.mu_unit)
i = identity.Identity(24)
v = velocity.Velocity(32)
t = time.Time(12)
l1 = l.multiply(24)
l2 = l.multiply(i)
l3 = v.multiply(t)

l1 = 24 * l
l1 = l * 24
l2 = i * l
l2 = l * i
l3 = v * t
l3 = t * v

try:
    v * l
except TypeError:
    pass
try:
    l * v
except TypeError:
    pass
```

The running result is consistent with the running result of the sample code of the Quantity.multiply method.

**Quantitiy.divide(self, other)**  
**Quantity.\__truediv__(self, other)**

The functions of these two functions are the same, and both express the division of physical quantities. According to the different types of the parameter ohter, the system will return different results.

1. If the parameter other is of type float or int, the return result is a physical quantity whose type is the same as this physical quantity, and the unit is the same as this physical quantity, except that its value is equal to the result of dividing the value of this physical quantity with other.
2. When other is an ohter non-Quantity type, a ValueError exception will be thrown
3. When ohter is a subtype Identity of Quantity, or when the physical quantity is Identity, the returned result is the same as the first case.
4. If other is of type Quantity or its subtypes, but the system cannot determine the type after division, it will throw TypeError exception.

Based on these characteristics, we can write the following code:

```python
from quantities import force
from quantities import time
from quantities import length

f = force.Force(53, force.ForceType.k_unit)
t = time.Time(5, time.TimeType.minute)
l = length.Length(33, length.LengthType.k_unit)

v = l.divide(t)
v = l / t
a = v.divide(t)
a = v / t
m = f.divide(a)
m = f / a

print(v.value)
print(v.current_unit.express_by_SI_base())
print(a.value)
print(a.current_unit.express_by_SI_base())
print(m.value)
print(m.current_unit.symbol())
```

The results of this code snippet are as follows:

```python
110.0
('m/s', 'm/s')
0.36666666666666664
('m\\cdot s^{-2}', 'm·s<sup>-2</sup>')
144545.45454545456
('kg', 'kg')
```

Because physical quantities have different physical meanings when dividing right by other types of data, we do not set the right dividing method in this API.

### Comparison operation

**Quantity.equal(self, other)**  
**Quantity.\__eq__(self, other)**

These two methods judge whether two physical quantities are equal. Its meaning is the same as the equality judgment of ordinary types.

1. The two physical quantities are equal only when the q_types of two instances of the class Quantity or its subclasses are equal, under the premise that they are all converted to the same unit, and their ```#!python value``` values are also equal.
2. When the parameter other is not an instance of Quantity or its subclasses, these two methods will throw a ValueError exception.
3. When parameter other is an instance of Quantity or its subclasses, but the q_types of the two are not the same, it means that they are not the same type of physical quantity. These two methods will throw a TypeError exception.

Using these two methods, we can write the following code:

```python
from quantities import force
from quantities import time
from quantities import length

l1 = length.Length(32, length.LengthType.k_unit)
l2 = length.Length(32000)
l3 = length.Length(320, length.LengthType.k_unit)
t = time.Time(32)

c1 = l1.equal(l2)
c1 = l1 == l2
c2 = l1.equal(l3)
c2 = l1 == l3
print(c1)
print(c2)

try:
    l1.equal(32000)
except ValueError as ex:
    print(ex)
try:
    l1 == 32000
except ValueError as ex:
    print(ex)

try:
    l1.equal(t)
except TypeError as ex:
    print(ex)
try:
    l1 == t
except TypeError as ex:
    print(ex)
```

The output after running this code snippet is:

```python
True
False
These two physical quantities can not be compared now!
These two physical quantities can not be compared now!
The two physical quantities are of different types!
The two physical quantities are of different types!
```

**Quantity.le(self, other)**  
**Quantity.\__le__(self, other)**

**Quantity.ge(self, other)**  
**Quantity.\__ge__(self, other)**

**Quantity.lt(self, other)**  
**Quantity.\__lt__(self, other)**

**Quantity.gt(self, other)**  
**Quantity.\__gt__(self, other)**

In these four groups of methods, each group has two methods with the same function, which have exactly the same meaning as the ordinary comparison method.

1. The q_types of two instances of the Quantity class or one of its subclasses are equal, and their ```#!python value``` values can be compared only when they are converted to the same unit.
2. When the parameter other is not an instance of Quantity or its subclasses, these two methods will throw a ValueError exception.
3. When parameter other is an instance of Quantity or its subclasses, but the q_types of the two are not the same, it means that they are not the same type of physical quantity. These two methods will throw a TypeError exception.

According to these four groups of methods, we can write the following code:

```python
from quantities import time
from quantities import length

l1 = length.Length(2, length.LengthType.k_unit)
l2 = length.Length(2001)
c1 = l2.gt(l1)
c1 = l2 > l1
c2 = l1.lt(l2)
c2 = l1 < l2

c3 = l2.ge(l1)
c3 = l2 >= l1
c4 = l1.le(l2)
c4 = l1 <= l2
t = time.Time(2, time.TimeType.k_unit)

print(c1)
print(c2)
print(c3)
print(c4)

try:
    l2 >= 2000
except ValueError as ex:
    print(ex)
try:
    l2 >= t
except TypeError as ex:
    print(ex)
```

The results of this code snippet are as follows:

```python
True
True
True
True
These two physical quantities can not be compared now!
The two physical quantities are of different types!
```

### Other methods

**Quantity.\__init__(self, value:float, q_type:QuantityType, unit=None)**  

This is the constructor of the physical quantity. Its first parameter ```#!python  value``` expresses the specific value of the physical quantity in a specific unit. It is a floating point number. The second parameter ```#!python q_type``` is the ```#!python QuantityType``` class or its subclasses. It expresses the type of this physical quantity. For example, the physical quantity of length, its type is ```#!python LengthType```. It determines the characteristics of this physical quantity. The third parameter ```#!python unit``` expresses the unit of some physical quantity. By default, the SI coherent unit of this type is selected.

Under normal circumstances, this constructor is rarely used. We would rather inherit the Quantity class to generate a new subclass for a certain physical quantity, and specify its physical quantity type in the subclass to determine its characteristics. For example, the ```#!python LengthType``` class is a subclass of ```#!python QuantityType```, which is the type we designed for the physical quantity of length. At the same time, we will design  class ```#!python Length```, which is the subclass of ```#!python Quantity```, to express the physical quantity of length, and directly specify its ```#!python q_type``` attribute in the constructor. For details, please refer to [Lenght].  

**Quantity.to_unit(self, unit)**：This method can achieve unit conversion, it will return a new Quantity or an instance of its subclass. Quantity and its subclasses are immutable object classes.  
If the parameter ```#!python unit``` does not match the physical quantity type expressed by an instance of Quantity or its subclass, the method will throw a ```#!python TypeError``` exception. For example, if an instance of  Quantity expresses the length physical quantity, but we pass in the unit of the mass physical quantity type in ```#!python to_unit```, or pass in None, it will throw a TypeError exception.
Using this method we can write the following code:

```python
from quantities import length

l1 = length.Length(2, length.LengthType.k_unit)
l_type = l1.q_type
l2 = l1.to_unit(l_type.SI_conherent_unit)

assert l2.value == 2000
```

### Three only-read properties

**Quantity.value(self)**：This is a getter property that expresses the specific value of this physical quantity in the currently selected unit condition. Only using this property and the  ```#!python current_unit``` property at the same time can fully express a physical quantity.  
**Quantity.q_type(self)**：This property expresses the type of this physical quantity.  
**Quantity.current_unit**：This property expresses the currently selected unit of this physical quantity。

## API of the QuantityType class  

```#!python QuantityType``` is a very important class. Based on it, the physical quantity type expressed by the instance of Quantity and its subclasses can be determined, and the available unit of a certain physical quantity type in the Physical Quantity Calculating system can also be determined according to it. Based on it, the system can determine the new physical quantity after the calculation.
Because each physical quantity has a unique type, only one instance of QuantityType is required for each physical quantity, and this instance is the class object of QuantityType and its subclasses, which has global uniqueness. Therefore, the programming interfaces we are going to discuss are all class properties and class methods.

### Available units

In Physical Quantity Calculating, the available units of a specific physical quantity can be obtained in QuantityType and its subclasses. They are divided into four categories.  

1. **QuantityType.pri_unit**  The first category is the primary unit. This unit is the starting point for designing other units. For example, the primary unit of the length unit is m, and the primary unit of the mass unit is g.

2. **QuantityType.SI_conherent_unit**  The second category is the coherent unit of the SI unit system. Generally, the primary unit of a physical quantity is often the same as its coherent unit, but there are exceptions. For example, in the mass unit, g is its primary unit, which facilitates the design of the entire system. But the coherent unit of its SI unit system is kg.

3. **20 properties such as QuantityType.g_unit**   The SI unit system design contains 20 prefix units to express the multiples or fractional units of its coherent unit. When the QuantityType was designed, these 20 units were naturally included. Its properties are in the form of prefix followed by _unit. For example, for the length quantity, its coherent unit is m, then its k prefix unit is km, which can be obtained from **LengthType.k_unit**。

4. **Other non-SI units**  In Physical Quantity Calculating, in addition to the SI unit system, some non-SI units of physical quantity, such as feet, inches and other units of length quantity, are also partially realized. There are corresponding class attributes in the subclasses of the corresponding QuantityType. For example, the length in feet can be obtained through LengthType.inch.  

According to the available unit interface of QuantityType, we can write the following code:

```python hl_lines="3 4"
from quantities import length

l1 = length.Length(2, length.LengthType.k_unit)
l2 = l1.to_unit(length.LengthType.inch)
print(l2.value)
print(l2.current_unit.symbol())
```

The results of this code snippet are as follows:

```python
78740.15748031497
('inch', 'inch')
```

### Register new QuantityType subclass

```#!python QuantityType``` and its subclasses have a class method ```#!python register_type```. It will register a subclass of ```#!python QuantityType``` with the system to let the system know how this type is obtained through arithmetic calculations. Generally, when designing a new ```#!python QuantityType``` subclass, you must override this method, but do not modify it during programming.

### QuantityType.source

All QuantityType and its subclasses have a ```#!python source``` property. This property points to a dictionary that contains information about all types of physical quantities. Generally, it is only necessary to add new content to the dictionary pointed to by ```#!python source``` by overriding its register_type class method when designing a subclass of QuantityType. When programming, **never modify** the ```#!python source``` so that it points to other content, and **do not modify** the content of the dictionary it points to.

For details about the ```#!python register_type``` method and the property ```#!python  source```, please refer to [Add A New Quantity](/add_new_quantity/)

## API of the Unit class

Unit expresses the unit of physical quantity. It only needs one instance, unlike Quantity, which requires multiple instances to express multiple instances of the same type of physical quantity. In the Pyhton programming language, a class is also an object, and the class object is unique in the global scope. Therefore, we use class objects to express various units of various types of physical quantities. Therefore, in Physical Quantity Calculating, the methods of Unit and its subclasses are all class methods. These methods are divided into three categories, one is used for unit conversion, the another is used for writing expression, and the last is ```#!python q_type``` property.  

### Unit conversion

It is only necessary to design two unit conversion methods for each unit, one is used for calculation of conversion from this unit to another unit, and the other is used for calculation of conversion from another unit to this unit. There are these two methods to ensure that the unit can be freely converted between the same type of physical unit. For details, see the pattern of Figure 3.3 in [UML Diagrams for Chapter 3 of Analysis Patterns](https://martinfowler.com/apsupp/apchap3.pdf)。

The two specific methods are as follows:  
**Unit.from_pri_unit(cls, value)**  
**Unit.to_pri_unit(cls, value)**  
The two specific methods are as follows. Their parameter value refers to the specific digital value in the current unit. For example, the current unit of the physical quantity of length is m, and its numerical value is 1000. It needs to be converted to a unit such as km. Such problems are often dealt with in Quantity.to_unit, the code is as follows:  

```python hl_lines="7 8"
class Quantity
    ......
    def to_unit(self, unit:Unit):
            if unit not in self.q_type.__dict__.values() or unit == None:
                raise TypeError('The unit is not for this physical qunatity!')
            else:
                to_pri_value = self.current_unit.to_pri_unit(self.__value)
                value = unit.from_pri_unit(to_pri_value)
                return Quantity(value, self.q_type, unit)
```

The meaning of pri_unit has been explained in the design of QuantityType, which can be seen [in detail](/add_new_quantity/).

### writing expression

There are usually three ways to write and express units in the SI unit system and other units that are not in the SI unit system. The first is to directly use the symbol of the unit to express the unit. The second is to use the power product of the basic unit of the SI unit system to express. The third is to use the power product of the basic unit of the SI unit system and the derived unit with a specific name to express.  
Writing may occur in Latex documents or html documents, and the way of expression is different. To this end, Unit provides a total of three methods, each of which can return the content expressed in the two documents. they are, respectively:
**Unit.symbol(cls)**  
**Unit.express_by_SI_base(cls)**  
**Unit.express_by_SI(cls)**  
Each method returns a tuple, which contains latex writing and html writing strings. The following code illustrates this:

```python
from quantities import length
from quantities import acceleration
from quantities import energy

l = length.Length(2)
a = acceleration.Acceleration(3)
e = energy.Energy(5)

print(l.current_unit.symbol())
print(a.current_unit.express_by_SI_base())
print(e.current_unit.express_by_SI())
```

The results of this code snippet are as follows:

```python
('m', 'm')
('m\\cdot s^{-2}', 'm·s<sup>-2</sup>')
('N\\cdot m', 'N·m')
```

### Unit.q_type class property

This property returns a class object of a subclass of QuantityType. It indicates that this unit can only be used for the physical quantity specified by ```#!python q_type```, and is a usable unit of this physical quantity type.
