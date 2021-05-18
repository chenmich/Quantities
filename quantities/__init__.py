import math

from .units import Unit
from .quantity import Quantity
from .quantity_type import QuantityType

from .identity import IdentityType, Identity, IdentityUnit

#the  SI base unit, 
#table2 in the https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?version=1.9&download=true
from .time import TimeType, Time, s
from .length import LengthType, Length, m
from .radial_length import RadialLengthType, RadialLength
from .mass import MassType, Mass, g
from .electric_current import ElectriCurrent, ElectriCurrentType, A
from .thermodynamic_temperature import ThermodynamicTemperatureType, ThermodynamicTemperature, K
from .amount_of_substance import AmountOfSubstanceType, AmountOfSubstance, mole
from .luminous_intensity import LuminousIntensityType, LuminousIntensity, cd

#The following are the derived units of the SI unit system

#the 22 SI units with special names and symbols
#table4 in the https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?version=1.9&download=true
from .plane_angle import PlaneAngleType, PlaneAngle, radian
from .solid_angle import SolidAngleType, SolidAngle, steradian
from .frequency import FrequencyType, Frequency, hertz
from .force import ForceType, Force, N
from .stress import StressType, Stress, pascal
from .energy import EnergyType, Energy, joule
from .work import Work, WorkType
from .amount_of_heat import AmountOfHeatType, AmountOfHeat
from .power import PowerType, Power, watt
from .electric_charge import ElectriChargeType, ElectriCharge, coulomb
from .electric_potential_difference import ElectricPotentialDifferenceType, \
                                                ElectricPotentialDifference, volt
from .capacitance import CapacitanceType, Capacitance, farad
from .electric_resistance import ElectricResistanceType, ElectricResistance, ohm
from .electric_conductance import ElectricConductanceType, ElectricConductance, siemens
from .magnetic_flux import MagneticFluxType, MagneticFlux, weber
from .magnetic_flux_density import MagneticFluxDensityType, MagneticFluxDensity, tesla
from .inductance import InductanceType, Inductance, henry


# some of coherent derived units in the SI expressed in terms of base units
#table5 in the https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?version=1.9&download=true
from .area import AreaType, Area, square_meter
from .volume import VolumeType, Volume, cubic_meter
from .radial_area import RadialAreaType, RadialArea
from .velocity import VelocityType, Velocity, m_per_s
from .acceleration import AccelerationType, Acceleration, meter_per_s_s
from .wavenumber import WavenumberType, Wavenumber, per_meter
from .density import DensityType, Density, kilogram_per_cubic_meter
from .surface_density import SurfaceDensityType, SurfaceDensity, kilogram_per_square_meter
from .specific_volume import SpecificVolumeType, SpecificVolume, cubic_meter_per_kilogram
from .current_density import CurrentDensityType, CurrentDensity, ampere_per_square_meter
from .magnetic_field_strength import MagneticFieldStrengthType, MagneticFieldStrength, ampere_per_meter
from .magnetic_permeability import MagneticPermeabilityType, MagneticPermeability, newton_per_square_ampere
from .electric_constant import ElectricConstantType, ElectricConstant, farad_per_meter
from .amount_of_substance_concentration import AmountOfSubstanceConcentrationType, \
                                                   AmountOfSubstanceConcentration, mole_per_cubic_meter
from .mass_concentration import MassConcentrationType, MassConcentration


#Examples of SI coherent derived units whose names and symbols
#include SI coherent derived units with special names and symbols
#table6 in the https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf/2d2b50bf-f2b4-9661-f402-5f9d66e4b507?version=1.9&download=true
from .gradient_speed_position import GradientSpeedPositionType, GradientSpeedPosition, per_second
from .dynamic_viscosity import DynamicViscosityType, DynamicViscosity, pascal_second
from .moment_of_force import MomentOfForceType, MomentOfForce, newton_meter
from .surface_tension import SurfaceTensionType, SurfaceTension, newton_per_meter
from .angular_velocity import AngularVelocityType, AngularVelocity, radian_per_second
from .angular_acceleration import AngulaAccelerationType, AngulaAcceleration, radian_per_second_squared
from .heat_flux_density import HeatFluxDensityType, HeatFluxDensity, watt_per_square_metre
from .heat_capacity import HeatCapacityType, HeatCapacity, joule_per_kelvin
from .entropy import EntropyType, Entropy
from .specific_heat_capacity import SpecificHeatCapacityType, SpecificHeatCapacity, joule_per_kilogram_kelvin
from .specific_energy import SpecificEnergyType, SpecificEnergy, joule_per_kilogram
from .gradient_temperature_position import GradientTemperaturePositionType, GradientTemperaturePosition, kelvin_per_meter
from .thermal_conductivity import ThermalConductivityType, ThermalConductivity, watt_per_meter_kelvin
from .energy_density import EnergyDensityType, EnergyDensity, joule_per_cubic_meter
from .electric_field_strength import ElectricFieldStrengthType, ElectricFieldStrength, volt_per_meter



#Constants
mu_0 = MagneticPermeability(4*math.pi*1e-7)
epsilon_0 = ElectricConstant(8.8541878128e-12)
g = Acceleration(9.8)
C = Velocity(299792458)


__version__ = '0.1.0'