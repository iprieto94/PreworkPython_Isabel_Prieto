'''Escribe un programa que determine si un número ingresado por el usuario es primo
o no.'''
def es_primo(num, n=2):
    if n >= num:
        print("Es primo")
        return True
    elif num % n != 0:
        return es_primo(num, n + 1)
    else:
        print("No es primo")
        return False

es_primo(33)