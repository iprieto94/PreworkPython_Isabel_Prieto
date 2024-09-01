'''Crea un programa que calcule el precio final de un artículo después de aplicar un
descuento del 20%.'''

def calculadora(Precio, Descuento):
  return Precio - (Descuento*Precio)/100
Precio_final = calculadora(150,20)
print ("El precio rebajado es de",Precio_final, "euros")

'''SOLUCION'''

def calcular_precio_final(precio):
  descuento = precio_original * 0.2
  total = precio_original - descuento
  return total

precio_original = float(input("Introduzca el precio del atículo: "))

precio_descuento = calcular_precio_final(precio_original)

print(f"El total a pagar, incluyendo la propina es: {precio_descuento}")