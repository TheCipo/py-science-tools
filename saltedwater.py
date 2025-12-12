#calculate the boiling point of water an salt
sodium_chloride = 58.44  # g/mol, molar mass of sodium chloride
kb = 0.512  # °C kg/mol, ebullioscopic constant for water
i = 1 + 1 * (2 - 1)

salt = float(input("Enter the amount of salt in grams: "))
water = float(input("Enter the amount of water in grams: "))

moles_salt = salt / sodium_chloride  # moles of salt
molatiy = moles_salt / (water / 1000)  # molality of the solution
increse_in_boil = i * kb * molatiy  # increase in boiling point
boiling_point = 100 + increse_in_boil  # boiling point of the solution
print(f"The boiling point of the solution is {boiling_point:.2f} °C")
