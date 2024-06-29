'''Crea un programa que convierta una cantidad de dólares a euros. Suponiendo que
1 dólar es igual a 0.85 euros.'''
#Opción A
Dólar = 1
Euros = 0.85
Cartera_dólares = 65
Cartera_euros = (Cartera_dólares*Euros)/Dólar
print (Cartera_euros)

#Opción B
def Conversor_moneda (Dólar, Euros, Cartera_dólares):
  return (Cartera_dólares*Euros)/Dólar
Cartera_euros = Conversor_moneda(1, 0.85, 65)
print (Cartera_euros)