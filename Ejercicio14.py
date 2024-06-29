'''Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.'''

def calculadora(Precio, Descuento):
  return Precio - (Descuento*Precio)/100
Precio_final = calculadora(150,20)
print ("El precio rebajado es de",Precio_final, "euros")