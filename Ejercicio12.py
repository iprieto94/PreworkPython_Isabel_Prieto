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