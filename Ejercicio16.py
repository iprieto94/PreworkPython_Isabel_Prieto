'''Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.'''

numeros = range (101)
suma_par = 0
suma_impar = 0
for numero in numeros:
 if numero % 2 ==0:
   suma_par = suma_par+1
 if numero %2 !=0:
     suma_impar = suma_impar+1
     print (suma_par, suma_impar)