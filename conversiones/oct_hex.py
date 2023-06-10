#-*-coding: utf-8 -*-
"""
Función que me permite pasar un octal a hexadecimal
"""
import oct_bin

def octal_a_hexadecimal(octal):
    
    binario = oct_bin.octal_a_binario(octal)  # Transformo el octal en binario
    dic = {"0001":"1","0010":"2","0011":"3","0100":"4","0101":"5","0110":"6","0111":"7","1000":"8","1001":"9","1010":"A","1011":"B","1100":"C","1101":"D" ,"1110":"E","1111":"F"}
    digito = ""
    hexa = ""
    ceros = len(binario) % 4  # Averiguo la cantidad de dígitos que quedan sin formar bloque de 4
    contador = 0

    if ceros != 0:  # Si hay un bloque incompleto
        ceros = (4 - ceros) * "0"  # Cantidad de ceros que faltan para formar el bloque 
        binario = ceros + binario  # Agrego los ceros al principio de la cadena

    for i in binario[::-1]:  # Recorro la cadena desde el final al principio
        contador += 1
        digito = i + digito  # Cadena ordenada

        if contador == 4:  # Si se forma bloque de 4
            contador = 0
            if digito in dic.keys():  # Itero por las claves del diccionario
                hexa = dic[digito] + hexa  # Guardo y ordeno el valor de la clave
                digito = ""

    return hexa
