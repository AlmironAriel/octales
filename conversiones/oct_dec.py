#-*-coding: utf-8 -*-
"""
Función que convierte un octal en decimal
"""

def octal_a_dec(octal):
        octal = str(octal)
        digitos = len(octal)  # Cantidad de digitos que posee el octal
        exponente = digitos - 1 
        decimal = 0

        for i in octal:  # Recorre cada valor del octal ingresado.
            potencia = 8 ** exponente  # Eleva 8 al exponente asignado anteriormente.
            resultado = potencia * int(i)  # Multiplica el resultado anterior por el valor del octal.
            decimal += resultado  # Cada resultado se sumará y se guardará.
            exponente -= 1  # Se resta el exponente para la próxima iteracion.

        
        return decimal
    
                
