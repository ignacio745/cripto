def transposicion(cadena: str, k: list[int]):
    nueva = ""
    for i in range(len(cadena)//len(k)):
        for j in k:
            nueva += cadena[i*len(k)+j-1]
    return nueva


if __name__ == "__main__":
    # print(transposicion("NO POR MUCHO MADRUGAR", [3, 7, 2, 6, 4, 1, 5]))
    # print(transposicion("  ORPNOCMU HMORRDAUAG", [6, 3, 1, 5, 7, 4, 2]))
    # print(transposicion("AHIVALABOMBA", [3,1,4,2]))
    print(transposicion("NOPORMUCHOMADRUGAR###", [3, 7, 2, 6, 4, 1, 5]))