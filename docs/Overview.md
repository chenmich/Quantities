# Overview

The Physical Quantities Calculating class library is developed in the Python 3.8.5 environment and is a class library that handles the calculating of physical quantities and the conversion of the measurement units. This library is fully close to the concept of physical quantity, and emphasizes the relationship between physical quantities. Automatically generate a new quantity after calculation, which is closer to the domain knowledge of quantity calculation. It can also handle unit conversion between [SI unit](https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?version=1.9&download=true).

## Feature

- There is only a simple interface for the arithmetic calculation of physical quantities and the selection of measurement units.  
- New types of physical quantities are automatically generated for calculation and automatic unit conversion.  
- It can handle most of the SI unit system units and non-SI unit system units selected by the SI unit system. For example, the minute, hour, day, month, and year of time, etc.  
- By simply subclassing the base class method, new physical quantities and their units of measurement can be easily generated for easy expansion.  
- Use Identity to express the concept of unitless quantity.  

## Install

### install frow PyPi

pip install quantities

### download

download from [git](https://github.com/chenmich/Quantities)

## Usage

```python
import quantities as pq
l = pq.Length(33)
t = pq.Time(11)
v = l / t
print(v.value)
print(v.current_unit.express_by_SI_base())

print()
a = v / t
print(a.value)
print(a.current_unit.express_by_SI_base())
```

The results after running the program are as follows:

```python
3.0
('m/s', 'm/s')

0.2727272727272727
('m\\cdot s^{-2}', 'm·s<sup>-2</sup>')

('km\\cdot s^{-2}', 'km·s<sup>-2</sup>')

('MN\\cdot m', 'MN·m')
('Mkg\\cdot m^{2}\\cdot s^{-2}', 'Mkg·m<sup>2</sup>·s<sup>-2</sup>')
```
