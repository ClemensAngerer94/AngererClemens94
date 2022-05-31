# Gartenparty Bsp



wetter = input("Wetter am Wochenende - Sonne oder Regen: ")
# doppeltes "==" Zeichen: Vergleichsoperator

if wetter.upper() == "Sonne":
    print("Gartenparty")
    print("Jawoooohl")
elif wetter.lower() == "regnereisch":
    print ("Kellerparty")
    print("Schaaadeeeee")
else:
    print (" entweder Sonne oder regnerisch eingeben!")