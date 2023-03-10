def busqueda_dicotomica_recursiva(tabla, elemento, inicio, fin):
    if inicio > fin:
        return -1
    medio = (inicio + fin) // 2
    if tabla[medio] == elemento:
        return medio
    elif tabla[medio] < elemento:
        return busqueda_dicotomica_recursiva(tabla, elemento, medio+1, fin)
    else:
        return busqueda_dicotomica_recursiva(tabla, elemento, inicio, medio-1)
