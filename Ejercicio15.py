'''Escribe un programa que convierta un número de minutos en horas y minutos. Por
ejemplo, 145 minutos serían 2 horas y 25 minutos.'''
def horas_minutos(minutos):
  horas = int(minutos/60)
  minutos_extra = minutos % 60
  return horas, minutos_extra

print(horas_minutos(930))