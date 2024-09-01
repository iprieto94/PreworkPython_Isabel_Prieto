'''Crea un programa que cuente y muestre la cantidad de números pares e impares en
una lista ingresada por el usuario.'''

numeros = range (100)
suma_par = 0
suma_impar = 0
for numero in numeros:
 if numero % 2 ==0:
   suma_par = suma_par+1
 if numero %2 !=0:
     suma_impar = suma_impar+1
print (suma_par, suma_impar)

'''SOLUCION'''

def contar_pares_impares(lista):
  pares = 0
  impares = 0
  for num in lista:
    if num % 2 ==0:
      pares = pares + 1
    else:
     impares +=1
  return pares, impares

numeros = list(map(int, input("Introduce una lista de numeros separados por espacios: ").split()))
pares, impares = contar_pares_impares(numeros)
print(f"La lista contiene {pares} numeros pares y {impares} numeros impares")