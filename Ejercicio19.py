'''Escribe un programa que determine si un año ingresado por el usuario es bisiesto o
no.'''
Año = 2000

if Año % 4 !=0 and Año % 100 !=0 and Año % 400 !=0:
  print ("Caso 1 El año ingresado no es bisiesto")
if Año % 4 ==0 and Año % 100 !=0 and Año % 400 !=0:
  print ("Caso 2 El año ingresado es bisiesto")
if Año % 4 ==0 and Año % 100 ==0 and Año % 400 !=0:
  print ("Caso 3 El año ingresado no es bisiesto")
if Año % 4 ==0 and Año % 100 ==0 and Año % 400 ==0:
  print ("Caso 4 El año ingresado es bisiesto")

