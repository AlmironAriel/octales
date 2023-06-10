# -*- coding: utf-8 -*-
"""
Función que convierte un octal en número romano
"""

def octal_a_romano(octal):
    octal = int(octal)
    lista_decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] 
    lista_romano = ['M', 'CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
    romano= ''
    i = 0
    while octal > 0:
        for x in range(octal//lista_decimal[i]):  
            romano += lista_romano[i]
            octal -= lista_decimal[i]
        i += 1

    return romano
 
