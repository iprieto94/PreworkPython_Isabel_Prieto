'''Crea un programa que calcule el área de un rectángulo. El usuario debe ingresar la
longitud y el ancho del rectángulo.'''
#Opción A
Altura = 5
Base = 15
Área = Altura * Base
print (Área)

#Opción B
def Área_rectángulo (Altura, Base):
  return Altura * Base
Área = Área_rectángulo (5, 15)
print (Área)

'''SOLUCION'''

def calcular_area_rectangulo(longitud, ancho):
  area = longitud * ancho
  return area

longitud = float(input("Introduce la longitud del rectangulo: "))
ancho = float(input("Introduce el ancho del rectangulo: "))

area_rectangulo = calcular_area_rectangulo(longitud, ancho)
print(f"El area del rectangulo es: {area_rectangulo}")