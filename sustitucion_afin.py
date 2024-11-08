from diccionario import diccionario, diccionario_inverso

def sustitucion_afin(cadena: str, N: int, a: int, b: int, k: int):
    nueva = ""
    for i in range(len(cadena)//2):
        bloque = cadena[i*2:i*2+2]
        x = 0
        j = 1
        for caracter in bloque:
            x += diccionario[caracter]*27**(len(bloque)-j)
            j += 1
        x = (a*x+b)%N
        nueva += f"{x}"
    return nueva

if __name__ == "__main__":
    print(sustitucion_afin("HAYGENTEQUEDESUCENCIATIENELACABEZALLENA", 131, 3, 7, 1))