'''Crea un programa que calcule el monto total a pagar en un restaurante, incluyendo
una propina del 15% sobre el total de la cuenta.'''
#Opción A
Cuenta = 25 + 13+ 55 + 17
Total = (Cuenta+(Cuenta*15)/100)
print (Total)

#Opción B
def calculadora(Cuenta):
  return (Cuenta+(Cuenta*15)/100)
Total = calculadora (25 + 13+ 55 + 17)
print (Total)
