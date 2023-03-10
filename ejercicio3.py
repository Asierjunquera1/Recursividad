def ordenar_fichas(fichas):
    n = len(fichas)
    i, j, k = 0, 0, n-1  
    while j <= k:
        if fichas[j] == 'rojo':
            fichas[i], fichas[j] = fichas[j], fichas[i]
            i += 1
            j += 1
        elif fichas[j] == 'verde':
            j += 1
        else:  
            fichas[j], fichas[k] = fichas[k], fichas[j]
            k -= 1
    return fichas
