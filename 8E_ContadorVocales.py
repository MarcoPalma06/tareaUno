#Marco Antonio Palma Rivera
#20192000607

def contarVocales(frase):
    frase = frase.lower()
    vocales = 'aeiou'
    contador = 0

    for letra in frase:
        if letra in vocales:
            contador += 1
    
    return contador

frase = input("Redacte una frase: ")

print(f"La frase -{frase}- tiene  {contarVocales(frase)} vocales.")