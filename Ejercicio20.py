'''Crea un programa que sume todos los números en una lista ingresada por el
usuario.'''

mi_lista = [8, 9, 3, 4, 5]
print(sum(mi_lista))

###### SOLUCION

def sumar_lista(lista):
  suma = 0
  for num in lista:
    suma += num
  return suma

numeros = list(map(int, input("Introduce una lista de numeros separados por espacios: ").split()))
resultado = sumar_lista(numeros)
print(f"La suma de los numeros en la lista es: {resultado}")

