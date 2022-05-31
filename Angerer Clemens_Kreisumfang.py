# Die Eingabe soll in einer eigenen Funktion erfolgen,in der sichergestellt wird,dass es sich
#    a) jedenfalls um eine Zahl handelt
#und
#    b) eine positive Zahl ensteht

import math

def eingabe():
    correct = False
    while correct =False: # so lange bis eine korrekte Eingabe erfolgt
        r_str=input("Radius:  ")
        try:
            r = float(r_str)
            if r > 0:
                correct = True
            else:
                print(" keine gültige Eingabe! (r <=0)")
        except VaueError:
            print("keine gültige Eingabe (keine Zahl)")
    return r

def kreisumfang(radius):
    umfang = 2*radius*3.14159265
    return umfang

kreisradius = Eingabe()
print ("eingegebener Radius: ", kreisradius)

umfang = kreisumfang(kreisradius)
print("Kreisumfang: ",umfang)
