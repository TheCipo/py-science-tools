import math
t = float(input("Enter the temperature °C: ")) + 273.15
p = float(input("Enter the pressure hPa: "))

# Calculate the ratio of standard temperature to actual temperature
temp_ratio = 288.15 / t

# Calculate the pressure ratio adjusted for temperature
pressure_ratio = (p / 1013.25) / (t / 288.15)

# Calculate the exponent for the formula
exponent = ((((9.81 * 0.0289) / (t * 8.314)) - 1) ** -1)

# Calculate density altitude using the broken-down formula
density_altitude = temp_ratio * (1 - pressure_ratio) ** exponent
pressure_altitude = (1 - (p / 1013.25) ** 0.190284) * 145366.45 * 0.3048  # in meters

# ISA temperature at pressure altitude
isa_temp = 15 - (pressure_altitude / 1000 * 2)  # lapse rate 2°C per 1000m

# Density altitude formula
density_altitude = pressure_altitude + 120 * ((t - 273.15) - isa_temp)
print(f"the density altitude is {density_altitude} m")
if(density_altitude > 1000):
    print("airtow operation is not allowed")
elif(density_altitude < 1000 and density_altitude > 870):
    print("airtow operation is allowed with caution")
else:
    print("airtow operation is allowed")
input("press enter to exit:")