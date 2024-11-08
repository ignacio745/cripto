from diccionario import diccionario, diccionario_inverso, diccionario_sin_ñ, diccionario_inverso_sin_ñ

def vigeniere(cadena: str, clave: str, dic: dict, dic_inv:dict):
    nueva = ""
    for i in range(len(cadena)):
        pos = dic[cadena[i]]
        pos_clave = dic[clave[i%len(clave)]]
        pos = (pos+pos_clave)%len(dic)
        nueva += dic_inv[pos]
    return nueva

def deshacer_vigeniere(cadena: str, clave: str, dic: dict, dic_inv:dict):
    nueva = ""
    for i in range(len(cadena)):
        pos = dic[cadena[i]]
        pos_clave = dic[clave[i%len(clave)]]
        pos = (pos-pos_clave)%(len(dic))
        nueva += dic_inv[pos]
    return nueva


if __name__ == "__main__":
    print(deshacer_vigeniere("OYXFQFJAHGGCPXANTOMNS", "HELLMAN", diccionario_sin_ñ, diccionario_inverso_sin_ñ))