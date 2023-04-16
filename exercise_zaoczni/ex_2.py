# trojkat
# deklaracja zmiennych 
from cmath import pi


a = 10
b = 12
c = 8
h = 6

obwod = a + b + c
pole = 1/2 * a * h 

print("Obwod trojkata wynosi " + str(obwod) + ", zas pole wynosi " + str(pole) + ".")

# romb

a = 5
h = 4

pole = a * h 
obwod = 4 * a 

print("Pole rombu wynosi " + str(pole) + ", zas obwod wynosi " + str(obwod) + ".")

# prostokat

a = 4
b = 5

pole = a * b 
obwod = (a+b)*2

print("Pole prostokata wynosi " + str(pole) + ", zas obwod wynosi " + str(obwod) + ".")

# trapez

a = 3
b = 28
c = 20
d = 15
h = 12

pole = (a+b)*h/2
obwod = a + b + c + d

print("Pole trapezu wynosi " + str(pole) + ", zas obwod wynosi " + str(obwod) + ".")

# kolo

import math

pi = math.pi
r = 5

pole = pi * r ** 2
obwod = 2 * pi * r

print("Pole kola wynosi " + str(pole) + ", zas obwod wynosi " + str(obwod) + ".")
