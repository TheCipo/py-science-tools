def heat(mass, t1, t2, c):
    dt = t2 - t1
    q = mass * dt * c
    return q

L = 334000
c_Ice = 2090
c_Water = 4186
mu = 0.8

mass = float(input("Insert the mass of the food in Kg: "))
power = float(input("Insert the power of the microwave in W: "))

print("Temperature input\n-The temperatures MUST be under 100°C\n-The final temperature MUST be equal or grater than the inital temperature")
tI = float(input("Insert the initial temperature of the food in °C (frezer -19, fridge 8): "))
tF = float(input("Insert the final temperature of the food in °C: "))


if (tI * tF <= 0):
    q1 = heat(mass, tI, 0, c_Ice)
    ql = mass * L
    q2 = heat(mass, 0, tF, c_Water)
    qt = q1 + ql + q2
elif tF > 0:
    qt = heat(mass, tI, tF, c_Water)
else:
    qt = heat(mass, tI, tF, c_Ice)

qt += qt * mu

seconds = qt/power
minutes = seconds // 60
secs = seconds % 60
print("to cook your food you need ", seconds ," seconds or ", minutes, "minutes and ", secs ," seconds")
input("press enter to exit:")