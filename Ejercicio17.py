'''Escribe un programa que convierta una distancia en millas a kilómetros. Sabiendo
que 1 milla equivale a 1.60934 kilómetros.'''

def Conversor_distancia (Millas, Km, Distancia_millas):
  return (Distancia_millas*Km)/Millas
Distancia_km = Conversor_distancia(1, 1.60934, 120)
print (Distancia_km)