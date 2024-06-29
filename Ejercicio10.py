'''Escribe un programa que determine el día de la semana correspondiente a un
número ingresado por el usuario (1 para lunes, 2 para martes, etc.).'''
semana = {'L':1, 'M':2, 'X':3, 'J':4, 'V':5, 'S':6, 'D':7}
for dia, valor in semana.items():
  print (dia, " ", valor)