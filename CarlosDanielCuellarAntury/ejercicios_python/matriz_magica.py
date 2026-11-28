matriz = []

# Pedir los 9 valores
for i in range(3):
    fila = []
    for j in range(3):
        valor = int(input(f"Valor fila {i + 1}, columna {j + 1}: "))
        fila = fila + [valor]
    matriz = matriz + [fila]

# Mostrar la matriz como tabla
print("\nMatriz:")
for i in range(3):
    print(matriz[i][0], matriz[i][1], matriz[i][2], sep="\t")

# Suma de cada fila
sumas_filas = []
for i in range(3):
    suma = 0
    for j in range(3):
        suma = suma + matriz[i][j]
    sumas_filas = sumas_filas + [suma]
    print(f"Suma fila {i + 1}: {suma}")

# Suma de cada columna
sumas_columnas = []
for j in range(3):
    suma = 0
    for i in range(3):
        suma = suma + matriz[i][j]
    sumas_columnas = sumas_columnas + [suma]
    print(f"Suma columna {j + 1}: {suma}")

# Diagonales
diag_principal = 0
diag_secundaria = 0
for i in range(3):
    diag_principal = diag_principal + matriz[i][i]
    diag_secundaria = diag_secundaria + matriz[i][2 - i]
print("Diagonal principal:", diag_principal)
print("Diagonal secundaria:", diag_secundaria)

# ¿Cuadrado mágico? Todo debe sumar igual que la diagonal principal
es_magico = True
if diag_secundaria != diag_principal:
    es_magico = False
for i in range(3):
    if sumas_filas[i] != diag_principal or sumas_columnas[i] != diag_principal:
        es_magico = False

if es_magico:
    print(f"¡Es un cuadrado mágico! Todas las sumas dan {diag_principal}.")
else:
    print("No es un cuadrado mágico.")
