'''Escribe un programa que solicite al usuario su año de nacimiento y calcule su edad
actual.'''
#Opción A
Fecha_nacimiento = 1994
edad = 2024 - Fecha_nacimiento
print (edad)

#Opción B
def Calculadora_edad (Fecha_nacimiento):
  return 2024 - Fecha_nacimiento
Edad = Calculadora_edad(1994)
print (Edad)

'''SOLUCION'''
def Calculadora_edad (anio_nacimiento):
  anio_actual = 2024
  edad = anio_actual - anio_nacimiento
  return edad

anio_nacimiento = int(input("Introduce tu año de nacimiento: "))
edad = Calculadora_edad(anio_nacimiento)

print(f"Tienes {edad} años.")