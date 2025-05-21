from funciones_matriz import *
from verificar_cuadrado_mag import *

def main():
    # Elegir ingreso manual o aleatorio
    Decision_usuario = input("¿Desea ingresar la matriz manualmente (M) o generarla aleatoriamente (A)? ").strip().upper()
    if Decision_usuario == 'M':
        n = int(input("Ingrese el tamaño de la matriz (n x n): "))
        matriz = ingresar_matriz(n)
    elif Decision_usuario == 'A':
        n = int(input("Ingrese el tamaño de la matriz (n x n): "))
        matriz = generar_matriz_aleatoria(n)
    else:
        print("Opción no válida. Ingrese 'M' para manual o 'A' para aleatorio.")
        return
    
    # Validar
    if not validar_matriz(matriz, n):
        print("La matriz no es válida.")
        return
    
    # Mostrar la matriz
    mostrar_matriz(matriz)
    # Verificar si es cuadrado mágico
    verificar_cuadrado_magico(matriz)

if __name__ == "__main__":
    main()