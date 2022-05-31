# ITGL Labor Übungen
#erstelle Programm, das in 10° - Schritten zwischen 0° und 180° den jeweiligen Cosinus Wert berechnet und anschließend ausgibt
import math

winkel_grad = 0

while winkel_grad <= 180:
    winkel_red = winkel_grad * math.pi / 180
    cosinus = math.cos(winkel_grad)
    print("Winkel : ", winkel_grad, "-> cosinus: ", cosinus)
    winkel_grad += 10