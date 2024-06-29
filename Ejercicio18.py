'''Crea un programa que cuente la cantidad de palabras en una oración ingresada por
el usuario.'''

Oracion = "Mi coche es blanco"
palabras = Oracion.split()
Count=0
for x in palabras:
  Count = Count +1
print (palabras, Count)