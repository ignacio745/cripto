import numpy as np

def transposicion_fila_columna(cadena: str, filas: int, columnas: int, k: list[int]):
    nueva = ""
    matriz = np.array(list(cadena)).reshape(filas, columnas)
    for i in range(len(k)):
        for j in range(filas):
            nueva += matriz[j][k[i]-1]
    return nueva

# def deshacer_transposicion_fila_columna(cadena: str, filas: int, columnas: int, k: list[int]):
#     nueva = ""
#     matriz = np.array(list(cadena)).reshape(filas, columnas)
#     for i in range(len(k)):
#         for j in range(filas):
#             nueva += matriz[j][k[i]-1]
#     return nueva

def deshacer_transposicion_fila_columna(cadena: str, filas: int, columnas: int, k: list[int]):
    nueva = ""
    para_matriz = []
    for i in range(len(cadena)//filas):
        actual = cadena[i*filas:i*filas+filas]
        para_matriz.append([i for i in actual])  
    matriz = np.array(para_matriz).reshape(columnas, filas).T
    print(matriz)
    for comp in k:
        print(matriz[:,comp-1])
    nueva_matriz = np.empty((7,3), dtype=str)
    for i in range(len(k)):
        nueva_matriz[i] = matriz[:,k[i]-1]
    print(nueva_matriz)
    for j in range(filas):
        for i in range(columnas):
            nueva += nueva_matriz[i][j]
    print(nueva)




if __name__ == "__main__":
    # resultado = transposicion_fila_columna("MEGUSTACOMERPAPAMECOM", 3, 7, [6,5,1,7,3,2,4])
    # print(resultado)
    # original = transposicion_fila_columna(resultado, 3, 7, [3,6,5,7,2,1,4])
    # print(original)
    # deshacer_transposicion_fila_columna("TPOSRCMCPAAMGMMEOAUEE", 3, 7, [3,6,5,7,2,1,4])
    deshacer_transposicion_fila_columna("FPNQCMOAAJXSXGTYHNFGO", 3, 7, [3,6,5,7,2,1,4])