def filtar_unir(texto):
    a= ''.join(filter(str.isalnum, texto))
    return a


def mayusculas(texto):
    a=texto.upper()
    return a


def quitar_tildes(texto):
    cambios = (
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
    )
    for a, b in cambios:
        texto = texto.replace(a, b).replace(a.upper(), b.upper())
    return texto





def palindromo(texto):
    a=filtar_unir(texto)
    b=mayusculas(a)
    c=quitar_tildes(b)
    l=0
    for i in range(len(c)):
        if c[i]==c[len(c)-1-i]:
            pass
        else:
            l+=1
    if l==0:
        print("¡Es un palindromo!")
    else:
        print("No es un palindromo")

texto=input("Introduzca su texto:")
palindromo(texto)


