import random

def ingresar_matriz(n):
    """
    Permite al usuario ingresar una matriz n x n.
    Devuelve la matriz ingresada como lista de listas.
    """
    matriz = []
    numeros_ingresados = set()
    
    for i in range(n):
        fila = []
        while len(fila) < n:
            try:
                valor = int(input(f"Ingrese el valor para la fila {i+1}, columna {len(fila)+1}: "))
                if valor < 1 or valor > n**2:
                    print(f"El valor debe estar entre 1 y {n ** 2}.")
                elif valor in numeros_ingresados:
                    print("El valor ya ha sido ingresado. Ingrese un número diferente.")
                else:
                    fila.append(valor)
                    numeros_ingresados.add(valor)
            except ValueError:
                print("Por favor, ingrese un número entero.")
        matriz.append(fila)
    return matriz

def generar_matriz_aleatoria(n):
    """
    Genera una matriz n x n con números aleatorios entre 1 y n^2.
    """
    # Genera lista de numeros del 1 al n^2 y los mezcla aleatoriamente
    numeros = list(range(1, n**2 + 1))
    random.shuffle(numeros)
    
    # Crea la matriz a partir de la lista ya mezclada
    matriz = []
    for i in range(n):
        fila = numeros[i * n: (i + 1) * n]
        matriz.append(fila)
        
    return matriz

def validar_matriz(matriz, n):
    """
    Valida si la matriz es un cuadrado mágico.
    """
    if len(matriz) != n or any(len(fila) != n for fila in matriz):
        print("La matriz no es cuadrada.")
        return False
    
    todos = [num for fila in matriz for num in fila]
    if any(num < 1 or num > n**2 for num in todos):
        print(f"Los números deben estar entre 1 y {n**2}.")
        return False
    
    if len(set(todos)) != n**2:
        print("Los números deben ser únicos.")
        return False
    
    print("La matriz es válida.")
    return True

def mostrar_matriz(matriz):
    print("\nMatriz:")
    for fila in matriz:
        for valor in fila:
            print(f"{valor:3}", end=" ")
        print()
