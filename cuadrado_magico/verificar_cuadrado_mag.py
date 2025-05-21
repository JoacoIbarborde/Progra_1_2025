def calcular_constante_magica(n):
    """
    Devuelve la constante magica para una matriz n x n
    """
    constante_magica = n * (n**2 + 1) // 2
    print(f"El resultado de la constante mágica es: {constante_magica}")
    return constante_magica

def verificar_filas(matriz, constante_magica):
    n = len(matriz)

    for i in range(n):
        suma_fila = 0
        for j in range(n):
            suma_fila += matriz[i][j]
        if suma_fila != constante_magica:
            print(f"La suma de la fila {i + 1} es {suma_fila}, no es igual a la constante mágica.")
            return False
    return True

def verificar_columnas(matriz, constante_magica):
    n = len(matriz)

    for j in range(n):
        suma_columna = 0
        for i in range(n):
            suma_columna += matriz[i][j]
        if suma_columna != constante_magica:
            print(f"La suma de la columna {j + 1} es {suma_columna}, no es igual a la constante mágica ({constante_magica}).")
            return False
    return True

def verificar_diagonal_principal(matriz, constante_magica):
    n = len(matriz)
    suma_diagonal = 0

    for i in range(n):
        suma_diagonal += matriz[i][i]

    if suma_diagonal != constante_magica:
        print(f"La suma de la diagonal principal es {suma_diagonal}, no es igual a la constante mágica ({constante_magica}).")
        return False
    return True

def verificar_diagonal_secundaria(matriz, constante_magica):
    n = len(matriz)
    suma_diagonal = 0

    for i in range(n):
        suma_diagonal += matriz[i][n - 1 - i]

    if suma_diagonal != constante_magica:
        print(f"La suma de la diagonal secundaria es {suma_diagonal}, no es igual a la constante mágica ({constante_magica}).")
        return False
    return True

def verificar_cuadrado_magico(matriz):
    """
    Verifica si la matriz es un cuadrado mágico.
    """
    n = len(matriz)
    constante_magica = calcular_constante_magica(n)

    if verificar_filas(matriz, constante_magica) and verificar_columnas(matriz, constante_magica) and verificar_diagonal_principal(matriz, constante_magica) and verificar_diagonal_secundaria(matriz, constante_magica):
        print("La matriz es un cuadrado mágico.")
        return True
    else:
        print("La matriz no es un cuadrado mágico.")
        return False