#-*-coding: utf-8 -*-
"""
Función que me permite pasar un octal a binario
"""

def octal_a_binario(octal):
    
    dic = {0: "000",1: "001",2: "010",3: "011",4: "100",5: "101",6: "110",7: "111"}
    octal = str(octal)
    binario = ""

    for digito in octal:  # Itero cada digito del octal y lo paso como clave            
        bin = dic[int(digito)]  # Obtengo el valor de esa clave 
        binario += bin

    return binario

