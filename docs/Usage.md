## Physical quantity modeling
Users always perform arithmetic operations such as addition, subtraction, multiplication, and division for physical quantities. These operations are the same, so the interfaces of their physical quantity objects are also the same. For this purpose, a class **Quantity** is used to express the physical quantity. It provides users with a general arithmetic operation interface, and also provides users with an interface to access this physical quantity type. Of course, it also provides operations for setting and obtaining the current unit of measurement.

Use the quantity type class to distinguish the type of physical quantity, for example, use class **LengthType** as the type of quantity object for length quantity. The quantity type is responsible for generating the corresponding SI unit, checking the legality of addition, subtraction, multiplication and division between two objects, generating a new quantity, and responsible for the unit conversion of the quantity.

Each physical quantity has its own unit of measurement. Use class Unit to express these units. Each type of physical quantity has its own set of units. These units are automatically created when creating the class of their physical quantity type, and can be selected by the user according to the corresponding type class.

## create a quantity instance
It is very simple to create an instance of a physical quantity, the following is a code example:
```python
import quantities as pq
q_type = pq.LengthType
current_u = q_type.G_unit
l = pq.Quantity(22, q_type, current_u)
```
If you use the default SI coherent unit, you do not need to give the unit to the constructor.
```python
import quantities as pq
q_type = pq.LengthType
l = pq.Quantity(22, q_type)
```
The unit of the quantity object of this length type is meter. If you want to convert to other units, such as kilometers, the code can be written as:
```python
l1 = l.to_unit(q_type.k_unit)
```
Set the unit of the quantity by the quantity type, such as LengthType, to ensure the corresponding relationship between the quantity and the unit.

For ease of use, Physical Quantity calculating has also designed a proprietary class for commonly used physical quantities. For example, the physical quantity of the length type is Length, which can be found in pq.
## quantity calculating
The calculation is also very simple. code show as below:
```python
import quantities as pq
q_type = pq.LengthType
l = pq.Quantity(22, q_type)
l1 = l.to_unit(q_type.k_unit)

t = pq.Time(11)
v = l1.divide(t)
print(v.value)
print(v.current_unit.symbol())
print(v.current_unit.express_by_SI())
print(v.current_unit.express_by_SI_base())
```
The unit of the calculation result is the SI coherent unit of the result quantity type.

Because there are three ways to express the SI unit, one is to use the symbol of the unit, for example, the basic unit uses its symbol to express the unit, and some derived units use the power product of the basic unit, and some also use the power product of basic unit and  the derived unit with the specific name. To express these measurement units in various documents, there are Latex expressions and html expressions, so the Unit class provides three methods for expressing a certain unit, and each method returns two expressions.

When writing a document, the method that needs to be used in the program is determined by the user. The user needs to fully understand the writing method of units in the SI unit system, and this professional domain knowledge.

It also supports calculations under traditional codes:
```python
import quantities as pq
q_type = pq.LengthType
l = pq.Quantity(22, q_type)
l1 = l.to_unit(q_type.k_unit)

t = pq.Time(11)
v = l1 / t
```
It also supports the calculation of physical quantities and single real numbers (or integers), such as:

```python
import quantities as pq
q_type = pq.LengthType
l = pq.Quantity(22, q_type)
l1 = l.to_unit(q_type.k_unit)

l2 = 32 * l1
l3 = l1 * 32
l4 = l1 / 32
```
However, the physical meaning of the calculation between a quantity and an integer or a real number is not clear. This way of writing is not recommended and I prefer to write the following code. This physical meaning is very clear.

```python
import quantities as pq
q_type = pq.LengthType
l = pq.Quantity(22, q_type)
l1 = l.to_unit(q_type.k_unit)

i = pq.Identity(32)
l2 = i * l1
l3 = l1 * i
l4 = l1 / i
```
Identity is a physical quantity without a unit. The calculation result of multiplication and division between it and any physical quantity is the same as that of the original physical quantity, which has a clear physical meaning.

Through this kind of clear knowledge of the type of new physical quantity generated at every step, we only need to be familiar with the modeling field, or with the help of domain experts, the bugs in the program will be reduced a lot, even if there is a bug, because the concept is clear, the debug is also It will be easier.