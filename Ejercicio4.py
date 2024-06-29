'''Crea un programa que cuente el número de vocales en una palabra ingresada por el
usuario.
'''
def contar_vocales(frase):
    voc = 0
    for letra in frase.lower():
        if letra == 'a' or letra == 'e' or letra == 'i' or letra =='o' or letra == 'u':
            voc=voc+1
    return voc
print(contar_vocales("RAMEN"))



