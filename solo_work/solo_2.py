def trojkat (bok_a, bok_b, bok_c,h_a):
    pole = bok_a * h_a / 2
    obwod = bok_a + bok_b + bok_c
    return pole, obwod #return kończy funkcje, to co niżej nie będzie wykonane 
    
print(f'Pole i obwod trojkąta wynoszą : {trojkat(10, 15, 12, 8)}')

def kolo (pi,r):
    pole = pi * (r**2)
    obwod = 2* pi*r
    return pole, obwod 

print(f'Pole i obwod koła wynoszą : {kolo(3.141592653589793,4)}')

def trapez (bok_a, bok_b, bok_c, bok_d, h_a):
    pole = 1/2 * (bok_a + bok_b) * h_a
    obwod = bok_a + bok_b + bok_c + bok_d
    return pole, obwod

print(f'Pole i obwod trapezu wynoszą : {trapez(9, 5, 6, 6 , 4)}')