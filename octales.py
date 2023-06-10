from conversiones import oct_rom, oct_bin, oct_dec, oct_hex
import os

def validacion(octal):  # Valida el octal ingresado
    octal = str(octal)
    restriccion = "89"  # Valores que no estan en el sistema octal
    bandera = True

    for valor in octal:  # Recorre el octal ingresado buscando un valor incorrecto
        if valor in restriccion:
            bandera = False

    return bandera      


corte = raw_input('Presione 1...continuar   0...salir: ')
corte = int(corte)

while corte == 1:
    os.system('')
    print('-----'*6)
    print('0. Octal a Romano: ')
    print('2. Octal a binario: ')
    print('10. Octal a decimal: ')
    print('16. Octal a hexadecimal: ')
    print('-----'*6)
    print('')
    
  # menu
    opcion = raw_input('Ingrese una opcion: ')
    opcion = int(opcion)
    os.system('cls')
    
    if opcion == 0 or opcion == 2 or opcion == 10 or opcion == 16:
        octal = raw_input('Ingrese un octal: ')
        octal = int(octal)
        os.system('cls')
        print('')
        bandera = validacion(octal)
        
        if bandera == True:  # Si no se encontro un valor incorrecto, ingresa  
            if opcion == 10:
                print 'El octal ingresado en decimal es:', oct_dec.octal_a_dec(octal)
            elif opcion == 2:
                print 'El octal ingresado en binario es:', oct_bin.octal_a_binario(octal)
            elif opcion == 16:
                print 'El octal ingresado en hexadecimal es:', oct_hex.octal_a_hexadecimal(octal)
            elif opcion == 0:     
                print 'El octal ingresado en romano es:', oct_rom.octal_a_romano(octal)
            else:
                bandera == False
                print 'Ingrese una opcion valida'
        else:
            print 'Numero octal no valido. por favor ingrese un octal valido'
            print ''
    else:
        print 'Por favor ingrese una opcion valida'
        print ''
    corte = raw_input('Presione 1...continuar   0...salir: ')
    corte = int(corte)
    os.system('cls')                    
