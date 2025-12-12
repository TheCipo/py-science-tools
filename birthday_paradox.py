anno = 365

x = float(input("Quante persone ci sono? "))
temp = 1

for i in range(1, int(x) + 1):
    temp = ((anno - i) / anno) * temp

temp = (1 - temp) * 100

print("\nLa possibilità che 2 persone su", x, "abbiano la stessa data di nascita è del", temp, "%")
input("press enter to exit:")