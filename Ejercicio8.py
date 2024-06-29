'''Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona.'''
#opción A
Peso = 69
Talla =1.67
IMC = Peso/pow(Talla,2)
print (IMC)

#opción B
def calculadora_IMC (Peso, Talla):
  return Peso/pow(Talla,2)
IMC = calculadora_IMC(69,1.67)
print (IMC)