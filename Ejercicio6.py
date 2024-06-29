'''Crea un programa que verifique si una palabra ingresada por el usuario es un
palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).'''

def es_palindromo(palabra):
  return palabra == palabra[::-1]
print(es_palindromo("radar"))
print(es_palindromo("Gato"))