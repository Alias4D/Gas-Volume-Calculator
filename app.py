import streamlit as st

def calculate_gas_volume(pressure, temperature, molar_mass, z, mass):
  """
  Calculates the volume of gas using the ideal gas law with compressibility factor.

  Args:
      pressure (float): Pressure in bar.
      temperature (float): Temperature in Celsius.
      molar_mass (float): Molar mass in g/mol.
      z (float): Compressibility factor (between 0.9 and 1).
      mass (float): Mass of the gas in kg.

  Returns:
      float: The volume of the gas in cubic meters (m³).
  """

  # Convert pressure to bar.g
  pressure = pressure + 1  

  # Convert temperature to Kelvin
  temperature_kelvin = temperature + 273.15

  # Convert molar mass to kg/mol
  molar_mass_kg = molar_mass / 1000

  # Gas constant
  gas_constant = 8.314e-5  # bar * m³ / mol * K

  # Ideal gas law with compressibility factor
  volume = (mass * z * gas_constant * temperature_kelvin) / (pressure * molar_mass_kg)

  return volume

st.set_page_config(page_title="Gas [ Mass 2 Volume ] Convertor",page_icon="🧮")

st.header(" 🧮 Gas [ Mass >>> Volume ] Convertor")
c1,c2 = st.columns(spec=[0.4,0.6],gap="large")

# Input fields
mass = c1.number_input("Mass (kg)", min_value=0.0 , value=1000.0)
pressure = c1.number_input("Pressure (bar.g)", min_value=0.0,value=35.0)
temperature = c1.number_input("Temperature (°C)", min_value=0.0,value=20.0)
molar_mass = c1.number_input("Molar Mass (g/mol)", min_value=2.0 , value=20.0)
z = c1.number_input("Compressibility Factor (Z)", min_value=0.9, max_value=1.0,value=0.99)

# Calculations
c2.subheader("Calculation Results : ")

a_volume = calculate_gas_volume(pressure, temperature, molar_mass, z, mass)
c2.info(f"Gas Volume @ Input Conditions [m3] = {a_volume:,.2f}")

n_volume = calculate_gas_volume(pressure=0.0, temperature=20.0, molar_mass=molar_mass, z=z, mass=mass)
c2.info(f"Gas Volume @ Normal Conditions [Nm3] = {n_volume:,.2f}")

s_volume = calculate_gas_volume(pressure=0.0, temperature=0.0, molar_mass=molar_mass, z=z, mass=mass)
c2.info(f"Gas Volume @ Standard Conditions [Sm3] = {s_volume:,.2f}")

c2.divider()
c2.write("By : 👨‍💻 Alias @ aliasalias85@gmail.com ")
