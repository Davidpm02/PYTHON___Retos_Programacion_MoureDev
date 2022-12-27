#/*
#* Crea un programa que invierta el orden de una cadena de texto
#* sin usar funciones propias del lenguaje que lo hagan de forma automática.
#* - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#*/


# En este reto dejaremos al usuario que proporciona la cadena que desee invertir.
# Haremos uso de un bucle for para recorrer la cadena, e ir anadiendo a una lista vacia cada letra desde el final de la cadena
# e.g.:
# string = 'food'
#
# iteracion n1:
# listaCadena = ['d']
#
# iteracion n2:
# listaCadena = ['d','o']
# ...
def invertirCadena():
    cadena = input('Introduzca una palabra:')
    
    listaCadena = []
    contadorNegativo = -1
    
    for letra in cadena[:]:
        listaCadena.append(cadena[contadorNegativo])
        contadorNegativo -=1
    
    
    palabraInvertida = ''.join(listaCadena)  # Cuando tenemos la lista completa tras haber recorrido la cadena,
    return palabraInvertida                  # hacemos uso del metodo join para formar la nueva cadena invertida.
                                             # NOTA: .join() es llamado desde lo que sera el separador entre los elementos de 
                                             # la lista pasada como argumento.


if __name__ == '__main__':
    print(invertirCadena())
        